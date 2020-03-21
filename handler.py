from matriks import Matriks

def readfile(namafile):
	state = Matriks()
	f = open(namafile, "r")
	f_baris = f.readlines()
	i = 0
	for baris in f_baris:
		x = baris.split()
		j = 0
		for y in x:
			state.pos[i][j] = y
			if(y != '*'):
				state.pos[i][j] = int(y)
			j += 1
		i += 1
	state.kosong = state.find('*')
	return state


