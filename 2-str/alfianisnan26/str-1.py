# Addition --> Proses penambahan untuk Angka (+)
# Concatenation --> Proses penambahan untuk Karakter (+)

firstName = "Alfian"
lastName = "Isnan"

# name = firstName + " " + lastName
# Manual Concat
print(
    "Halo {0}, Selamat Pagi :)\n" +
    "Nama Lengkap : \"{0} {1}\"".format(firstName, lastName))

# Anonymous Format
name = "{} : {} {}"
formattedName = name.format(firstName, lastName, firstName)
print(formattedName)

# Indexed Format
indexedName = "{0} : {1} {0}"
formattedName = indexedName.format(firstName, lastName)
print(formattedName)

# Named Format
namedName = "{fn} : {ln} {fn}"
formattedName = namedName.format(ln=lastName, fn=firstName)
print(formattedName)

template = "Halo {fn}, Selamat Pagi :)\nNama Lengkap : \"{fn} {ln}\""
kalimat = template.format(fn=firstName, ln=lastName)
print(kalimat)

# Halo Alfian, Selamat Pagi :)
# Nama Lengkap : "Alfian Isnan"

# Interpolation
kalimat = f"Nama Lengkap : {firstName} {lastName}"
print(kalimat)


