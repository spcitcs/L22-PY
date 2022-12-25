import os

# kumpulan fungsi menu
def selamatDatang():
    print("Halo, selamat datang di aplikasi saya")

def menu():
    print("Pilih menu : ")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print()
    print("0. Keluar")

def inputMenu():
    nomorMenu = int(input("Masukkan pilihan : "))
    return nomorMenu

def inputDuaAngka():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua   : "))
    return angka1, angka2

def tampilkanHasil(hasil):
    print(f"Hasil operasi : {hasil}")

def batasLayar():
    for i in range(25):
        print("=", end="")
    print()

# kumpulan fungsi operasi
def pertambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b

# fungsi menu utama
def menuUtama():
    batasLayar()
    menu()
    pilihanMenu = inputMenu()

    if pilihanMenu == 1: # pertambahan
        print("Operasi pertambahan")

        angka1, angka2 = inputDuaAngka()
        hasil = pertambahan(angka1, angka2)
        tampilkanHasil(hasil)

    elif pilihanMenu == 2: # pengurangan
        print("Operasi pengurangan")

        angka1, angka2 = inputDuaAngka()
        hasil = pengurangan(angka1, angka2)
        tampilkanHasil(hasil)

    elif pilihanMenu == 3: # perkalian
        print("Operasi perkalian")
        
        angka1, angka2 = inputDuaAngka()
        hasil = perkalian(angka1, angka2)
        tampilkanHasil(hasil)

    elif pilihanMenu == 4: # pembagian
        print("Operasi pembagian")
        
        angka1, angka2 = inputDuaAngka()
        hasil = pembagian(angka1, angka2)
        tampilkanHasil(hasil)

    elif pilihanMenu == 0:
        print("Keluar")
        return False

    else:
        print("Pilihan anda salah")

    return True

# program utama
if __name__ == "__main__":
    selamatDatang()

    masihJalan = True

    while masihJalan:
        masihJalan = menuUtama()

    print("Program Selesai")





    