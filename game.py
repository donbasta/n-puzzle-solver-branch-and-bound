from matriks import Matriks
from handler import readfile

namafile = input("Ketikkan nama filenya, ekstensinya juga ya:) : ")
state_awal = readfile(namafile)

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
	