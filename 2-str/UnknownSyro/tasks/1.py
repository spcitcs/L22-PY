# Task 1
# Aplikasi sederhana biodata


firstname = "M Syahril"
Lastname = "Alifasa"
Kelas = "x-4"
Tingkat = 10
title = "Gaya hidup berkelanjuran"
Rombel = 4

Data1= """\t\t Selamat Datang di dasbor
       
        Data[1]-----------------
        #Data Diri
        Nama\t\t: {fn} {ln}
        Nama depan\t: {fn}
        Nama Belakang\t: {ln}
        
        #Data Sekolah
        Kelas\t\t: {ks}
        Tingkat\t\t: 10
        Judul Proyek\t: {jp}
        Rombel\t\t: 4

        #Data Media Sosial
        Instagram\t: syahril_1311      (https://www.instagram.com/syahril_1311/)
        Github\t\t: UnknownSyro       (https://github.com/UnknownSyro) 
        Facebook\t: M Syahril ALifasa (https://www.facebook.com/phansyro.phansyro)
        """  
y = Data1.format(fn = firstname, ln = Lastname, ks = Kelas , jp = title )
print(y)


firstname = "Satyo"
lastname = "Trisandya"
kelas = "10-7"
tingkat = 10
title = "Kewirausahaan"
rombel = 7

x = """\t\tSelamat datang di dasbor

    Data [1]
    Nama\t\t: {fn} {ln}
    Kelas\t\t: {cl}
    Nama Depan\t\t: {fn}
    Nama Belakang\t: {ln}
    Tingkat\t\t: {gr}
    Judul Proyek\t: {tl}
    Rombel\t\t: {rl}

    \t\tData Sosial Media
    Intagram\t: tyosk_13 (https://instagram.com/tyosk_13)
    Facebook\t: {fn} {ln} (https://www.facebook.com/satyo.trisandya.1)
    Github\t: TyosK (https://github.com/TyosK)"""

y = x.format(fn=firstname, ln=lastname, cl=kelas, gr=tingkat, tl=title, rl=rombel)
print (y)



