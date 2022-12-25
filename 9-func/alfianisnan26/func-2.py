def selamatDatang():
    print("Halo, selamat datang di aplikasi saya")

def inputNama():
    hasil = input("Masukkan nama anda : ")
    return hasil

def sambutan(nama):
    print(f"Halo, {nama}. Ada yang bisa saya bantu?")

selamatDatang()
nama = inputNama()
sambutan(nama)