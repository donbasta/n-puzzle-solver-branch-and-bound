from matriks import Matriks
from handler import readfile

namafile = input("Ketikkan nama file, ekstensinya juga ya: ")
state_awal = readfile(namafile)

print(f"Matriks posisi awal yang dibaca dari {namafile} adalah sebagai berikut:")
print(f"{state_awal}")


for i in range(1,17):
	print(f"Nilai dari KURANG({i}) adalah: {state_awal.kurang(i)}")

print(f"Nilai dari total fungsi KURANG dan X adalah: {state_awal.cek()}")

state_awal.solve()
