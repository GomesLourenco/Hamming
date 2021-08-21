binary = [1,0,1,1]
x1= (binary[0] + binary[1] + binary[3])%2
x2= (binary[0] + binary[2] + binary[3])%2
x3 = (binary[1] + binary[2] + binary[3])%2

binary.insert(0,x1)
binary.insert(1,x2)
binary.insert(3,x3)

print(binary)

binary.pop(3)
binary.insert(3,0)
print(binary)

a = (binary[3] + binary[4] + binary[5] + binary[6])%2
b = (binary[1] + binary[2] + binary[5] + binary[6])%2
c = (binary[0] + binary[2] + binary[4] + binary[6])%2

print(a)
print(b)
print(c)





