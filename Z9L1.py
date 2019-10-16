import cmath

print("podaj z")
z = input()
z = complex(z)
print("z =", z)

modul_z = abs(z)
print("|z| =",modul_z)

argument_z = cmath.phase(z)
print("argument z =", argument_z)

sprzezenie_z = z.conjugate()
print("sprzezenie z =", sprzezenie_z)
