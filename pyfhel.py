from Pyfhel import Pyfhel, PyPtxt, PyCtxt
he = Pyfhel()
he.contextGen(p=65537)
he.keyGen()

p1 = he.encode(8)
p2 = he.encode(4)

c1 = he.encrypt(8.3876786)
c2 = he.encrypt(4.3876786)


c3 = c1 + c2
print(c3)
c3 = he.decrypt(c3)
print(he.decode(c3))
#print(type(he.decode(c3)))