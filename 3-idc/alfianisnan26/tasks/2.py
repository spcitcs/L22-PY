print("Halo, selamat datang di aplikasi database")
firstName   = input("Masukkan Nama Depan       : ") 
lastName    = input("Masukkan Nama Belakang    : ")
kelas       = input("Masukkan Kelas            : ")
judulProyek = input("Masukkan Judul Proyek     : ")
rombel      = input("Masukkan Rombel           : ")
ig          = input("Masukkan Instagram        : ")
lin         = input("Masukkan Linkedin         : ")

print()
print(f"""<Data Saya>
Nama          : {firstName} {lastName}
Nama Depan    : {firstName}
Nama Belakang : {lastName}

Data Sekolah
Kelas         : {kelas}-{rombel}
Judul Proyek  : "{judulProyek}"
 
Data Sosial Media
Instagram     : {ig} (https://instagram.com/{ig})
LinkedIn      : {lin} (https://linkedin.com/in/{lin})""")