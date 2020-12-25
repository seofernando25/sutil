from mat import Matrix44

a = Matrix44()
print(a.dat)
a.dat[0] = [4,7,9,10]
a.dat[1] = [2,3,3,8]
a.dat[2] = [8,10,2,3]
a.dat[3] = [3,3,4,8]

b = Matrix44()
print(b.dat)
b.dat[0] = [3,10,12,18]
b.dat[1] = [12,1,4,9]
b.dat[2] = [9,10,12,2]
b.dat[3] = [4,12,4,10]

print((a*b).dat)