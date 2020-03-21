from matriks import Matriks
from handler import readfile

print("Selamat datang di aplikasi 15-puzzle solver!")
print("Buat file konfigurasi awal permainan di file terpisah ya!")
namafile = input("Ketikkan nama filenya, ekstensinya juga ya:) : ")
state_awal = readfile(namafile)

print(f"Matriks posisi awal yang dibaca dari {namafile} adalah sebagai berikut:")

print("---------------")
print(f"{state_awal}")
print("---------------")

print()

for i in range(1,17):
	print(f"Nilai dari KURANG({i}) adalah: {state_awal.kurang(i)}")

print()

print(f"Nilai dari total fungsi KURANG dan X adalah: {state_awal.cek()}")

print()

state_awal.solve()
