print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @")

a = int(input('Masukkan angka dari a: '))
b = int(input('Masukkan angka dari b: '))
c = int(input('Masukkan angka dari c: '))
if a > b and a > c:
  print('Angka terbesar adalah', a)
elif b > a and b > c:
  print('Angka terbesar adalah', b)
else:
  print('Angka terbesar adalah', c)