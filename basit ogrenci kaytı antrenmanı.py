import sqlite3 as sql

class Ogreci:
    def __init__(self, gelenad, gelensoyad, gelenuni, gelenders, gelenvize1, gelenvize2, gelenfinal):
        self.ad = gelenad
        self.soyad = gelensoyad
        self.uni = gelenuni
        self.ders = gelenders
        self.vize1 = gelenvize1
        self.vize2 = gelenvize2
        self.final = gelenfinal
        self.con = sql.connect('student.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS graduate (adı TEXT, soyadı TEXT, uni TEXT, ders TEXT, ortalama INT)''')

    def orthesap(self):
        return (self.vize1 * 0.3) + (self.vize2 * 0.3) + (self.final * 0.4)

    def datayukle(self):
        self.cur.execute("INSERT INTO graduate (adı, soyadı, uni, ders, ortalama) VALUES (?, ?, ?, ?, ?)",
                         (self.ad, self.soyad, self.uni, self.ders, self.orthesap()))
        self.con.commit()
        self.con.close()

def kullanici_girdisi_al():
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı giriniz: ")
    uni = input("Üniversitenizi giriniz: ")
    ders = input("Ders giriniz: ")
    vize1 = int(input("1.Vize notunuzu giriniz: "))
    vize2 = int(input("2. Vize notunuzu giriniz: "))
    final = int(input("Final notunuzu giriniz: "))
    return ad, soyad, uni, ders, vize1, vize2, final

if __name__ == "__main__":
    ad, soyad, uni, ders, vize1, vize2, final = kullanici_girdisi_al()
    ogrenci = Ogreci(ad, soyad, uni, ders, vize1, vize2, final)
    ogrenci.datayukle()
