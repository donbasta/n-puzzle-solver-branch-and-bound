from matriks import Matriks
from handler import readfile

namafile = input("Ketikkan nama filenya, ekstensinya juga ya:) : ")
state_awal = readfile(namafile)

print("Petunjuk permainan:")
print("U: geser ke atas")
print("D: geser ke bawah")
print("R: geser ke kanan")
print("L: geser ke kiri")
print("*: kotak kosong")

cur = state_awal

t = 1
print(cur)
print("------------------")
while not cur.sol():
	print(f"step{t}: ", end = '')
	step = input()
	if step == 'L':
		cur = cur.move('x',-1)
	elif step == 'R':
		cur = cur.move('x',1)
	elif step == 'U':
		cur = cur.move('y',-1)
	elif step == 'D':
		cur = cur.move('y',1)
	print(cur)
	print("------------------")
	t += 1
	