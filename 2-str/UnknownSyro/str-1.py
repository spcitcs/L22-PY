from email.utils import formatdate
from tokenize import Name


print("hello world")
# Addition ---> Proses penambahan untuk angka (+)
# Concatenation ---> Proses Penambahan  untuk karakter (+)

firstName = "Syahril"
lastname = "alifasa"
name = firstName + " " + lastname
print(name)

# Expected: (print nya cuma sekali)
print(
    "halo " + firstName +", Selamat Pagi :v \nNama lengkap : \""+ name + "\"")
# Anonymous Format
Name ="{} : {} {}"
formattedname = Name.format(firstName, lastname, firstName)
print(formattedname)

# Indexed Format
indexedName = "{0} : {1} {0}"
formattedname = indexedName.format(firstName, lastname)
print(formattedname)
# Named Format
namedName = "{fn} : {ln} {fn} "



template = "hallo {fn}, Selamat pagi:)\n " + "nama lengkap : \"{fn} {ln}\""
formattedname = template.format(fn=firstName, ln=lastname)
print(formattedname)

#interpolation
Kalimat =f"Nama Lengkap : {firstName} {lastname}"
print(Kalimat)
Kalimat = f"halo syahril, selamat pagi\n" f"nama lengkap : {firstName} {lastname} "
print(Kalimat)