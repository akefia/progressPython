a = int(input("Masukkan nilai a:"))
b = int(input("Masukan nilai b:"))
print ("Operasi Aritmatik")
print ("+ (Penjumlahan)")
print ("- (Pengurangan)")
print ("* (Perkalian)")
print ("/ (Pembagian)")

operasi = input ("Masukkan Operator")
if operasi == '+':
    hasil = a + b
elif operasi == '-':
    hasil = a - b
elif operasi == '*':
    hasil = a * b
elif operasi == '/':
    if b !=0:
        hasil = a / b
    else:
        "Pembagian 0 Tidak Boleh"
else:
    "Operator tidak ditemukan"
print (f"Hasil: {a} {operasi} {b} = {hasil}")
