# username yang terdaftar
username = ("Allya Putri Ditya")
password = ("2309116078")

print("\n===LOGIN===\n") #menampilkan judul
username_1 = (input("Masukkan nama : ")) #masukan nama yang terdaftar
password_1 = (input("Masukkan NIM : ")) #masukan NIM yang terdaftar

if username_1 == username and password_1 == password : #perintah jika username dan NIM sesuai dan terdaftar, program akan lanjut jalan
    print ("\n===Login berhasil, selamat datang!===\n") #jika nama dan NIM sesuai, akan menampilkan ini
    print ("\n===PROGRAM MENGHITUNG NILAI KOVERSI KILOGRAM KE SATUAN MASSA YANG LAIN===\n") #menampilkan judul
    Angka = float(input("\nMasukkan angka : ")) #input angka yang ingin di konversikan
    print('Konversikan ke = \n 1. Pounds (lb)\n 2. Ounce (ons)\n 3. Gram (g)\n') #menampilkan pilihan satuan massa yang ingin dikonversikan kemana
    operasi = input("Silahkan pilih angka = ") #pilih satuan massa yang tersedia untuk di konversikan

    if operasi == "1": #jika memilih angka 1
        hasil = Angka *2.205 #rumus untuk mendapatkan hasil konversi yang sesuai
        print (f'\nKonversi dari {Angka} kg = {hasil} lb\n') #mencetak hasil dari rumus yang sudah dibuat sebelumnya
    elif operasi == "2": #jika memilih angka 2
        hasil = Angka * 35.274 #rumus untuk mendapatkan hasil konversi yang sesuai
        print (f'Konversi dari {Angka} kg = {hasil} ons\n') #mencetak hasil dari rumus yang sudah dibuat sebelumnya
    elif operasi == "3": #jika memilih angka 3
        hasil = Angka * 1000 #rumus untuk mendapatkan hasil konversi yang sesuai
        print (f'Konversi dari {Angka} kg = {hasil} g\n') #mencetak hasil dari rumus yang sudah dibuat sebelumnya
    else: #jika tidak memilih ketiga pilihan diatas
        print('\nKonversi gagal, silahkan pilih angka yang tersedia\n') #tampilan jika input nilai diluar dari pilihan
else:
    print ("\n===Login gagal, silahkan coba lagi!===\n") #jika nama dan NIM tidak terdaftar atau tidak sesuai akan menampilkan ini