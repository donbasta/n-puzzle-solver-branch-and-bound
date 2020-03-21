import copy
from queue import PriorityQueue
from time import perf_counter_ns

class Matriks:

	def __init__(self):
		self.pos = [[0 for i in range(4)] for i in range(4)]
		self.pos[3][3] = '*'
		self.kosong = [3,3]

	def bound(self):
		tidakPas = 0
		for i in range(4):
			for j in range(4):
				if self.pos[i][j] == '*':
					continue
				elif self.pos[i][j] != i*4+j+1:
					tidakPas += 1
		return tidakPas

	def findKosong(self):
		return self.kosong

	def move(self, arah, delta):
		next_state = copy.deepcopy(self)
		emp = next_state.kosong
		if arah == 'x':
			if delta == 1:
				if emp[1] == 3:
					# print("Langkah tidak valid")
					return None
				else:
					next_state.pos[emp[0]][emp[1]] = next_state.pos[emp[0]][emp[1]+1]
					next_state.pos[emp[0]][emp[1]+1] = '*'
					next_state.kosong[1] += 1
			elif delta == -1:
				if emp[1] == 0:
					# print("Langkah tidak valid")
					return None
				else:
					next_state.pos[emp[0]][emp[1]] = next_state.pos[emp[0]][emp[1]-1]
					next_state.pos[emp[0]][emp[1]-1] = '*'
					next_state.kosong[1] -= 1
		elif arah == 'y':
			if delta == 1:
				if emp[0] == 3:
					# print("Langkah tidak valid")
					return None
				else:
					next_state.pos[emp[0]][emp[1]] = next_state.pos[emp[0]+1][emp[1]]
					next_state.pos[emp[0]+1][emp[1]] = '*'
					next_state.kosong[0] += 1
			elif delta == -1:
				if emp[0] == 0:
					# print("Langkah tidak valid")
					return None
				else:
					next_state.pos[emp[0]][emp[1]] = next_state.pos[emp[0]-1][emp[1]]
					next_state.pos[emp[0]-1][emp[1]] = '*'
					next_state.kosong[0] -= 1
		return next_state

	def find(self, num):
		ans = [-1,-1]
		for i in range(4):
			for j in range(4):
				if self.pos[i][j] == num:
					ans = [i,j]
		return ans

	def kurang(self, num):
		if(num == 16):
			loc = self.kosong
		else:
			loc = self.find(num)
		linear = [self.pos[i//4][i%4] for i in range(16)];
		start = loc[0]*4+loc[1]
		if linear[start] == '*':
			linear[start] = 16
		res = 0
		for i in range(start+1,16):
			if linear[i] == '*':
				linear[i] = 16
			if linear[i] < linear[start]:
				res += 1
		return res

	def cek(self):
		res = 0
		for i in range(1,17):
			res += self.kurang(i);
		if (self.kosong[0]+self.kosong[1])%2 != 0:
			res += 1
		return res

	def valid(self):
		return (self.cek()%2==0)

	def solve(self):
		if not self.valid():
			print("Nilainya ganjil!.")
			print("\nOleh karena itu, puzzle ini tidak mungkin diselesaikan, maaf :(")
		else:
			t_start = perf_counter_ns()
			par, bangkit = self.bnb()
			t_finish = perf_counter_ns()
			waktu = (t_finish - t_start) / 1000
			print("Nilainya genap!!!!.")
			print("\nYey, puzzle ini dapat diselesaikan, hore :D")
			print("Dengan menggunakan algoritma Branch n Bound, solusinya adalah sebagai berikut:")

			solution = []
			target = Matriks()
			for i in range(4):
				for j in range(4):
					target.pos[i][j] = i*4+j+1
			target.pos[3][3] = '*'

			while(target != self):
				solution.append(target)
				target = par[target]
			solution.append(self)
			solution.reverse()

			idx = 0
			print("---------------")
			for state in solution:
				print(f"Step {idx}:\n\n{state}\n---------------")
				idx += 1

			print(f"Waktu eksekusi algoritmanya adalah: {waktu} mikro sekon")
			print()
			print(f"Banyak simpul yang dibangkitkan saat pencarian adalah {bangkit}")

	def sol(self):
		ok = True
		for i in range(4):
			for j in range(4):
				if i==3 and j==3:
					if self.pos[i][j] != '*':
						ok = False 
				elif self.pos[i][j] != i*4+j+1:
					ok = False
		return ok

	def bnb(self):
		vis = {self:True}
		bangkit = 1
		par = {}
		ketemu = False
		dist = {}
		setattr(Matriks, "__lt__", lambda self, other: self.bound()+dist[self] <= other.bound()+dist[self])
		li = PriorityQueue()
		li.put(self)
		dist[self] = 0
		while not li.empty():
			expand = li.get()
			for step in [['x',1],['x',-1],['y',1],['y',-1]]:
				child = expand.move(step[0],step[1])
				if child is not None:
					if child not in vis:
						par[child] = expand
						dist[child] = dist[expand] + 1
						bangkit += 1
						li.put(child)
						vis[child] = True
					if child.sol():
						ketemu = True
			if ketemu:
				break

		return par, bangkit

	def bnb1(self, vis, par, bangkit, ketemu):
		solution = [-1,-1,-1]
		q = []
		expand = self
		for step in [['x',1],['x',-1],['y',1],['y',-1]]:
			child = expand.move(step[0],step[1])
			if child is not None:
				if child not in vis:
					par[child] = expand
					bangkit += 1
					q.append(child)
					vis[child] = True
				if child.sol():
					ketemu = True

		if ketemu:
			return vis, par, bangkit, ketemu

		q.sort(key=lambda x : x.bound())

		for next_move in q:
			vis, par, bangkit, ketemu = next_move.bnb(vis, par, bangkit, ketemu)
			if ketemu:
				break

		return vis, par, bangkit, ketemu

	def __eq__(self, other):
		return str(self) == str(other)

	def __hash__(self):
		return hash(str(self))

	def __str__(self):
		res = ""
		for i in range(4):
			for j in range(4):
				res += str(self.pos[i][j])
				if j < 3:
					res += " "
			if i < 3:
				res += "\n"
		return res