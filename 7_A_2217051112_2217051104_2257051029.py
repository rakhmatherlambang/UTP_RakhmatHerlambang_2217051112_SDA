# Program Kantin Modern Jessy
# SDA RESPONSI
# 1. Rakhmat Herlambang (2217051112)
# 2. M. Fakhri Wilova   (2217051104)
# 3. Devrinatasyah      (2257051029)

from datetime import datetime
import os

nama_kelompok = ["1. Rakhmat Herlambang 2217051112", '2. M. Fakhri Wilova 2217051104', '3. Devrinatasyah 2257051029']
print("Nama Kelompok : ")
for kelompok in nama_kelompok:
    print(kelompok)

class KantinJessy:
    def __init__(self, nama_kantin):
        self.nama_kantin = nama_kantin
        
    def sambut_pelanggan(self):
        print(f'Selamat Datang di {self.nama_kantin}')

                
toko = KantinJessy('Kantin Jessy Modern')
toko.sambut_pelanggan()


print('-----------------------------------------------------------')
print('|                                                         |')
print('|                   Kantin Jessy                          |')
print('|                                                         |')                
print('-----------------------------------------------------------\n')
print('', end='\n')

total1 = 0
jenis1 = ""
porsi = 0

total2 = 0
jenis2 = ""
gelas = 0

pilihan = "beli"

while pilihan == "beli":

	def fungsimakanan():
		global total1
		global porsi
		global jenis1
		print("Menu Makanan")
		print("1. Nasi Goreng        : Rp 15000")
		print("2. Ayam Goreng        : Rp 17000")
		print("3. Pecel Lele         : Rp 13000")
		print("4. Risol KWU          : Rp 2000")
		print()

		nomor = int(input("Masukan Pilihan (Angka): "))
		porsi = int(input("Berapa Porsi (Angka): "))

		if nomor == 1:
			total1 = porsi * 15000
			print(porsi, " porsi Nasi Goreng = Rp", total1)
			jenis1 = ("Nasi Goreng")
		elif nomor == 2:
			total1 = porsi * 17000
			print(porsi, " porsi Ayam Goreng = Rp", total1)
			jenis1 = ("Ayam Goreng")
		elif nomor == 3:
			total1 = porsi * 13000
			print(porsi, " porsi Pecel Lele = Rp", total1)
			jenis1 = ("Pecel Lele")
		elif nomor == 4:
			total1 = porsi * 2000
			print(porsi, " porsi Risol KWU = Rp", total1)
			jenis1 = ("Risol KWU")
		else:
			print("Pilihan tidak ada, silahkan masukan")
	fungsimakanan()

	def fungsiminuman():
		global total2
		global jenis2
		global gelas
		print("Menu Minuman")
		print("1. Es Cincau KWU     : Rp 7000")
		print("2. Es Kopet          : Rp 5000")
		print("3. Es Teh            : Rp 3000")
		print("4. Es Buah KWU       : Rp 7000")
		print()

		nomor = int(input("Masukan Pilihan (Angka): "))
		gelas = int(input("Berapa Gelas (Angka): "))
		
		if nomor == 1:
			total2 = gelas * 7000
			print(gelas, " Es Cincau KWU = Rp", total2)
			jenis2 = ("Es Cincau KWU")
		elif nomor == 2:
			total2 = gelas * 5000
			print(gelas, " Es Kopet = Rp", total2)
			jenis2 = ("Es Kopet")
		elif nomor == 3:
			total2 = gelas * 3000
			print(gelas, " Es Teh = Rp", total2)
			jenis2 = ("Es Teh")
		elif nomor == 4:
			total2 = gelas * 7000
			print(gelas, " Es Buah KWU = Rp", total2)
			jenis2 = ("Es Buah KWU")
		else:
			print("Pilihan tidak ada, silahkan masukan lagi!!")
			fungsiminuman()

	fungsiminuman()

	totalsemua = 0
	totalsemua = total1 + total2

	print()
	print("Total harus dibayar: Rp", totalsemua)
	print()



	print("=======================================")
	print("========S T R U K P E S A N A N========")
	print("=======================================")
	print(" Makanan    : ", porsi, jenis1, ":", total1)
	print(" Minuman    : ", gelas, jenis2, ":", total2)
	print(" Tagihan    : Rp.", totalsemua)
	print("	Tanggal	   : ",datetime.now())
	print("=========== KASIH KE KASIR ============")
 

	beli = str(input("Apakah anda akan membeli lagi? [y/t] : "))

	if beli == "y":
		pass
	elif beli == "t":
		break

	
os.system("cls")