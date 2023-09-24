# username yang terdaftar
username = ("Allya Putri Ditya")
password = ("2309116078")

print("\n===LOGIN===\n")
username_1 = (input("Masukkan nama : "))
password_1 = (input("Masukkan NIM : "))

if username_1 == username and password_1 == password :
    print ("\n===Login berhasil, selamat datang!===\n")
    print ("\n===PROGRAM MENGHITUNG NILAI KOVERSI KILOGRAM KE SATUAN MASSA YANG LAIN===\n")
    Angka = float(input("\nMasukkan angka : "))
    print('Konversikan ke \n 1. Pounds (lb)\n 2. Ounce (ons)\n 3. Gram (g)\n')
    operasi = input("Silahkan pilih angka = ")

    if operasi == "1":
        hasil = Angka *2.205
        print (f'\nKonversi dari {Angka} kg = {hasil} lb\n')
    elif operasi == "2":
        hasil = Angka * 35.274
        print (f'Konversi dari {Angka} kg = {hasil} ons\n')
    elif operasi == "3":
        hasil = Angka * 1000
        print (f'Konversi dari {Angka} kg = {hasil} g\n')
    else:
        print('\nKonversi gagal, silahkan pilih angka yang tersedia\n')
else:
    print ("\n===Login gagal, silahkan coba lagi!===\n")