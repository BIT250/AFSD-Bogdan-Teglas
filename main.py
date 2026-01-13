tabla = [[".", ".", "."],
		 [".", ".", "."],
		 [".", ".", "."]]

nr_linii = len(tabla)
nr_coloane = len(tabla[0])

def afiseaza(tabla):
	for i in range(nr_linii):
		for j in range(nr_coloane):
			print(tabla[i][j], end=" ")
		print()

afiseaza(tabla)


# matrice patratica (nr_linii == nr_coloane)
# tabla = [[".", ".", "."],		(0,0) (0,1) (0,2)
# 		  [".", ".", "."],		(1,0) (1,1) (1,2)
# 		  [".", ".", "."]]		(2,0) (2,1) (2,2)
# diaganala principala: (0,0), (1,1), (2,2) conditia i == j
# diagonala secundara: (0,2), (1,1), (2,0) conditia i + j == nr_linii - 1

A = [[1, 2, 3],
	 [4, 5, 6],
	 [7, 8, 9]]

# diagonala principala
for i in range(nr_linii):
	for j in range(nr_coloane):
		if i == j:
			print(A[i][j])

# diagonala secundara
for i in range(nr_linii):
	for j in range(nr_coloane):
		if i + j == nr_linii - 1:
			print(A[i][j])