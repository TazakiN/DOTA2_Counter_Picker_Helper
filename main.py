from bs4 import BeautifulSoup
from itertools import islice
import requests

# inisiaisasi set / himpunan global
must_play = set()
dont_play = set()
hero_yang_sudah_diinput = set()

# baca file dota_heroes.txt
with open("dota_heroes.txt", "r") as f:
    dota_heroes = [line.rstrip().replace(" ", "_") for line in f]


def splash_screen():
    # print my ascii art splash screen in red
    print("\033[91m")

    print(
        """
 __  __ ___     __    __                         
|  \\/  \\ |  /\\   _)  |__). _|  __ |__| _| _  _ _ 
|__/\\__/ | /--\\ /__  |   |(_|(    |  |(-||_)(-|  
                                         |      
        """
    )


splash_screen()


def main():
    global must_play, dont_play, hero_yang_sudah_diinput

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
    elif nama_hero == "Kotl":
        nama_hero = "Keeper_of_the_Light"
    elif nama_hero not in dota_heroes:
        print("\033[91mHero tidak ditemukan\033[0m")
        main()
    elif nama_hero in hero_yang_sudah_diinput:
        print("\033[91mHero sudah diinput\033[0m")
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
            elif tag["id"] == "Works_well_with...":
                # menghentikan pencarian jika sudah menemukan tag dengan id "Works_well_with..."
                break
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
                # Secara tidak langsung, akan melakukan operasi gabungan antara himpunan must_play sebelumnya dengan must_play hero yang baru
                # atau must_play (sebelumnya) ∪ must_play (hero yang baru)
                must_play.add(tag["title"])
            elif flag == "good":
                # Secara tidak langsung, akan melakukan operasi gabungan antara himpunan dont_play sebelumnya dengan dont_play hero yang baru
                # atau dont_play (sebelumnya) ∪ dont_play (hero yang baru)
                dont_play.add(tag["title"])

    # hapus nama hero dan semua nama hero yang sudah diinput dari set must_play dan dont_play
    # must_play - hero_yang_sudah_diinput
    must_play.difference_update(hero_yang_sudah_diinput)
    # dont_play - hero_yang_sudah_diinput
    dont_play.difference_update(hero_yang_sudah_diinput)

    # Melakukan operasi selisih antara himpunan must_play dan dont_play
    # must_play - dont_play
    must_play.difference_update(dont_play)

    # Secara keseluruhan, operasi yang dilakukan adalah
    # (must_play (sebelumnya) ∪ must_play (hero yang baru)) - (dont_play (sebelumnya) ∪ dont_play (hero yang baru)) - hero_yang_sudah_diinput

    # ambil 10 hero pertama dari must_play
    top_heroes = list(islice(must_play, 10))

    # Menampilkan nama hero lawan di hero_yang_sudah_diinput
    # dengan warna hijau
    print("Hero yang dimainkan lawan:", end="")
    for hero in hero_yang_sudah_diinput:
        print(f"\033[92m {hero.replace('_', ' ')}\033[0m,", end="")
    # Menghilangkan koma di akhir
    print("\b \n")
    # Menampilkan nama hero yang harus dimainkan
    print("Hero yang baik untuk dimainkan:")
    for i, hero in enumerate(top_heroes, start=1):
        print(f"{i}. {hero}")
    print()

    print(
        "ketik \033[31mreset\033[0m untuk mengosongkan set atau \033[31mexit\033[0m untuk keluar dari program"
    )
    main()


if __name__ == "__main__":
    main()
