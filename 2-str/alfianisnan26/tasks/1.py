# Task 1
# Aplikasi sederhana biodata

# Selamat datang di dasbor...
#
# Data [1] -----------------------------
# Data Diri
# Nama          : Alfian Isnan
# Nama Depan    : Alfian
# Nama Belakang : Isnan
#
# Data Sekolah
# Kelas         : 12-7-Belajar Python
# Tingkat       : 12
# Judul Proyek  : "Belajar Python"
# Rombel        : 7
# 
# Data Sosial Media
# Instagram     : alf.ian (https://instagram.com/alf.ian_)
# LinkedIn      : alfian-isnan (https://linkedin.com/in/alfian-isnan)
#
# Data [2] -----------------------------
# Data Diri
# Nama          : Alfian Isnan
# Nama Depan    : Alfian
# Nama Belakang : Isnan
#
# Data Sekolah
# Kelas         : 12-7-Belajar Python
# Tingkat       : 12
# Judul Proyek  : "Belajar Python"
# Rombel        : 7
# 
# Data Sosial Media
# Instagram     : alf.ian (https://instagram.com/alf.ian_)
# LinkedIn      : alfian-isnan (https://linkedin.com/in/alfian-isnan)
#
# Data [3] -----------------------------
# Data Diri
# Nama          : Alfian Isnan
# Nama Depan    : Alfian
# Nama Belakang : Isnan
#
# Data Sekolah
# Kelas         : 12-7-Belajar Python
# Tingkat       : 12
# Judul Proyek  : "Belajar Python"
# Rombel        : 7
# 
# Data Sosial Media
# Instagram     : alf.ian (https://instagram.com/alf.ian_)
# LinkedIn      : alfian-isnan (https://linkedin.com/in/alfian-isnan)

tName = "Nama \t\t: {} {}"
tFName = "Nama Depan\t: {}"
tLName = "Nama Belakang\t: {}"

fn1 = "Alfian"
ln1 = "Isnan"

fn2 = "Gentha"
ln2 = "Ardaana"

format = """Nama\t\t: {fn} {ln}
Nama Depan\t: {fn}
Nama Belakang\t: {ln}\n"""

print(format.format(fn=fn1, ln=ln1))
print(format.format(fn=fn2, ln=ln2))

print(tName.format(fn1, ln1))
print(tFName.format(fn1))
print()
# print(tName.format(fn2, ln2))
# print(tFName.format(fn2))
