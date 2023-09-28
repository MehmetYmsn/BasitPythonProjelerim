

from random import randint
def carpim(a, b, c):
    if c != "-1":
        result = str(a * b)
        if result == c:
            print("\t\t***** Doğru *****")
        else:
            print("\t!!! Yanlış, cevap {} olacak.".format(result))
            secim()
    else:

        secim()


def basla(sayi1, sayi2):
    if sayi1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            sayi_1 = randint(sayi1, sayi2)
            sayi_2 = randint(sayi1, sayi2)
            print("_" * 50, "\n")
            print("{} x {} kaça eşittir? (çıkış = -1)".format(sayi_1, sayi_2))
            sonuc = input("sonuc >> ")
            carpim(sayi_1, sayi_2, sonuc)

            if i == 4 and j == 4:
                print("\n *-- Tebrikler bir sonraki bölüme geç!! --*\n")
                secim()


def secim():
    print(" Bir seviye seç. (çık = -1) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    svy = input(" >> ")

    if svy == "1":
        basla(1, 6)

    elif svy == "2":
        basla(6, 12)

    elif svy == "3":
        basla(12, 25)

    elif svy == "4":
        basla(25, 100)

    else:
        exit(0)


if __name__ == '__main__':
    secim()
