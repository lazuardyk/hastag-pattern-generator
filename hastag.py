def RataKanan(rows):
  for i in range(rows):
    for j in range(rows-i+1):
      print("", end=" ")
    for x in range(i+1):
      print("#", end="")
    print()

def RataKiri(rows):
  for i in range(rows):
    for j in range(i+1):
      print("#", end="")
    print()

def Segitiga(rows):
  for i in range(rows):
    for j in range(rows-i+1):
      print("", end=" ")
    for x in range(i+1):
      print("#", end=" ")
    print()

def Catur(rows):
  for i in range(rows):
    for j in range(rows):
      if (i+j) % 2 == 0:
        print("#", end="")
      else:
        print(" ", end="")
    print()

Message = "PROGRAM BENTUK PAGAR"
Message2 = "#" * 50
print('{:^80}'.format(Message2))
print('{:^80}'.format(Message))
print('{:^80}'.format(Message2))
laz = int(input("\nMasukkan jumlah baris yang diinginkan:"))
laz2 = input("Bentuk rata kanan, kiri, segitiga, atau papan catur? (kanan/kiri/segitiga/catur):")
if laz2 == "kanan":
  RataKanan(laz)
elif laz2 == "kiri":
  RataKiri(laz)
elif laz2 == "catur":
  Catur(laz)
elif laz2 =="segitiga":
  Segitiga(laz)
else:
  print("Masukkan kanan/kiri/segitiga/catur!")
