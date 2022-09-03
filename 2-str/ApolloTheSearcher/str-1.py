# Concatenation --> (Penggabungan Kata) proses penambahan untuk menambahkan huruf notasinya (+)
# Addition ( + ) --> proses penambahan angka

first_name = "Gentha" # snake_case penulisannya dibedakannya dengan menggunakan underscore
lastName = "Ardaana" # camelCase penulisannya dibedakan dari N besarnya sebagai pengganti spasi
samaDengan = "="

''' => Comment
# Proses concatenation
name = first_name + " " + lastName
name1 = first_name + "=" +  lastName
name2 = first_name + samaDengan + lastName
print("Challenge 1")
print("cara 1:", name1)
print("cara 2 :", name2)
ucapan = f"Hallo {first_name}, Selamat Pagi 😆"
dataDiri = f'Nama Lengkap : "Gentha Ardaana"'

print("---------------------------------------------")

# Selamat Pagi Ucapan
print("Selamat Pagi Challenge")
print(f"Hallo {first_name}, Selamat Pagi 😆")
print("==============================================")
# Challenge 2
print("Challenge 2")
print(ucapan + "\n" + dataDiri)
print("===============================================")

print("Hallo " + first_name + ", Selamat Pagi :)\n"
        + "Nama Lengkap : \""+name+"\"")



# Anonymous Format
name = "Nama : {} {}"
formattedName = name.format(first_name, lastName)
print(formattedName)

name = "{} : {} {}"
formatedName = name.format(first_name, lastName ,first_name)
print(formatedName)


# Index Formatting
indexName = "{0} : {1} {0}"
formatedNameIndex = indexName.format(first_name, lastName)
print(formatedNameIndex)

# Named Formatting
namedFormatting = "{gen} : {ard} {gen}"
namedFormattingFormat = namedFormatting.format(gen = first_name, ard = lastName)
''' # => Multiple Comment

# Tugas
# Hallo Gentha Ardaana, Selamat Pagi
# Nama Lengkap : "Gentha Ardaana"

print("Hallo {0}, Selamat Pagi\nNama Lengkap : \"{0} {1}\"😆".format(first_name, lastName))
namedTugas = "Hallo {fn}, Selamat Pagi, \nNama Lengkap : \"{fn} {ln}\""
kalimat = namedTugas.format(fn = first_name, ln = lastName)
print(kalimat)


# Interpolition
print(f"Nama Lengkap : {first_name} {lastName}")
kalimat = f"Hallo Gentha, Selamat Pagi 😆 \nNama Lengkap : \"{first_name} {lastName}\""
print(kalimat)