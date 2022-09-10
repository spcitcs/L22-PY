# Task 1
# Aplikasi sederhana biodata

# Selamat datang di dasbor...

# ------------------------------ Data Diri [1] ----------------------------------
# Nama              : Nama Kalian
# Nama Depan        :
# Nama Belakang     :

# Data Sekolah
# Nama Sekolah      : SMAN 1 CIBADAK
# Kelas             : Kelas Kalian
# Tingkat           : 12
# Jurusan           : IPA
# Rombel            : 3

# Data Sosial Media
# Instagram         : (Yang ada linknya)
# LinkedIn          : (Yang ada linknya)

# Selamat datang di dasbor...


# ------------------------------ Data Diri [2] ----------------------------------
# Nama              : Nama Kalian
# Nama Depan        :
# Nama Belakang     :

# Data Sekolah
# Nama Sekolah      : SMAN 1 CIBADAK
# Kelas             : Kelas Kalian
# Tingkat           : 12
# Jurusan           : IPA
# Rombel            : 3

# Data Sosial Media
# Instagram         : (Yang ada linknya)
# LinkedIn          : (Yang ada linknya)

# Selamat datang di dasbor...

# ------------------------------ Data Diri [3] ----------------------------------
# Nama              : Nama Kalian
# Nama Depan        :
# Nama Belakang     :

# Data Sekolah
# Nama Sekolah      : SMAN 1 CIBADAK
# Kelas             : Kelas Kalian
# Tingkat           : 12
# Jurusan           : IPA
# Rombel            : 3

# Data Sosial Media
# Instagram         : (Yang ada linknya)
# LinkedIn          : (Yang ada linknya)

# Memakai formatting dan menggunakan variable nya
nameList = ["Gentha", "Jokowi", "Prabowo"]
lastName = ["Ardaana", "Widodo", "Subianto"]
kelas = ["12 IPA 3", "12 IPS 2", "12 IPS 1"]
for name in range(len(nameList)):
    welcome = "Selamat datang di dasbor..."
    header = f"""---------------------------------- Data Diri [{name + 1}]---------------------------------
    Nama            : {nameList[name] +" "+ lastName[name]}
    Nama Depan      : {nameList[name]} 
    Nama Belakang   : {lastName[name]}
---------------------------------- Data Sekolah ------------------------------------------------
    Nama Sekolah    : SMAN 1 CIBADAK
    Kelas           : {kelas[name]}
    """
    print(header)