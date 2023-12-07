from bs4 import BeautifulSoup
from itertools import islice
import requests

# inisiaisasi set dan list
must_play = set()
dont_play = set()
hero_yang_sudah_diinput = set()

# baca file dota_heroes.txt
with open("dota_heroes.txt", "r") as f:
    dota_heroes = [line.rstrip() for line in f]


def main():
    global must_play, dont_play

    # input nama hero
    nama_hero = (
        input("\033[94mMasukkan nama hero lawan: \033[0m")
        .title()
        .strip()
        .replace(" ", "_")
    )
    if nama_hero == "Exit":
        exit()
    elif nama_hero == "Reset":
        must_play = set()
        dont_play = set()
        hero_yang_sudah_diinput = set()
        print("Set telah direset")
        main()
    elif nama_hero not in dota_heroes:
        print("\033[91mHero tidak ditemukan\033[0m")
        main()

    # Mengambil data dari website dota2.fandom.com sesuai dengan nama hero
    url = f"https://dota2.fandom.com/wiki/{nama_hero}/Counters"
    hero_yang_sudah_diinput.add(nama_hero)
    response = requests.get(url)
    with requests.get(url) as response:
        soup = BeautifulSoup(response.content, "html.parser")

    # Inisialisasi flag
    flag = None

    # Cari tag <a> dan <span> yang memiliki atribut id
    for tag in soup.find_all(["a", "span"]):
        if "id" in tag.attrs:
            if tag["id"] == "Bad_against...":
                flag = "bad"
            elif tag["id"] == "Good_against...":
                flag = "good"
        elif (
            flag
            and tag.name == "a"
            and "title" in tag.attrs
            and tag["title"] in dota_heroes
        ):
            if flag == "bad":
                # jika hero tersebut sudah ada di must_play, tempatkan di urutan pertama
                if tag["title"] in must_play:
                    must_play.remove(tag["title"])
                    must_play.add(tag["title"])
                else:
                    must_play.add(tag["title"])
            elif flag == "good":
                dont_play.add(tag["title"])

    # hapus nama hero dan semua nama hero yang sudah diinput dari set must_play dan dont_play
    must_play.difference_update(hero_yang_sudah_diinput)
    dont_play.difference_update(hero_yang_sudah_diinput)

    # pastikan tidak ada hero di must_play yang ada di dont_play
    must_play.difference_update(dont_play)

    # ambil 10 hero pertama dari must_play
    top_heroes = list(islice(must_play, 10))

    print("Hero yang baik untuk dimainkan:")
    for i, hero in enumerate(top_heroes, start=1):
        print(f"{i}. {hero}")
    print()

    print(
        "ketik \033[31mreset\033[0m untuk mengosongkan set dan \033[31mexit\033[0m untuk keluar dari program"
    )
    main()


if __name__ == "__main__":
    main()
