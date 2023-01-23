#CONTOH FUNCTION
def biodata():
    nama = "Daven Gabriel"
    nim  = "\n20210801043"
    jrsn = "\nTeknik Informatika"
    bio = nama + nim + jrsn
    print("\nCONTOH FUNCTION")
    print(bio)
biodata()

#CONTOH RECURSIVE
def faktorial(a): 
  if (a > 1):
    return a * faktorial(a-1)
  else:
    return 1
print("\nCONTOH RECURSIVE")
angka = int(input('Input angka: '))
 
print(angka,'! = ',faktorial(angka))

