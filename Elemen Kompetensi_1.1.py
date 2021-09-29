print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @")
print("KALKULATOR PHYTAGORAS")
from math import sqrt
tes = input('Sisi mana yang ingin anda hitung? (a, b, c): ')

if tes == 'c':
    A =int(input("masukkan panjang sisi a= "))
    B=int(input("masukkan panjang sisi b= "))

    C=sqrt(A * A + B*B)
    print('panjang dari sisi C adalah',C)

elif tes== 'a':
    C=int(input("masukkan panjang sisi c= "))
    B=int(input("masukkan panjang sisi b= "))
if (C<B):
    print("Panjang c tidak valid!")
    C=int(input("masukkan panjang sisi c= "))
    
    A=sqrt(C * C - B*B)
    print('panjang dari sisi A adalah', A)

elif tes== 'b':
    C=int(input("masukkan panjang sisi c= "))
    A=int(input("masukkan panjang sisi a= "))
    if (A>C):
       print("Panjang c tidak valid!")
    C=int(input("masukkan panjang sisi c= "))

    B=sqrt(C*C - A*A)
    print('panjang dari sisi B adalah',B)
