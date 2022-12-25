# Cara penulisan fungsi

# Fungsi tanpa input, dan tanpa output
def fungsi1():
    print("fungsi1 ini adalah fungsi tanpa input dan tanpa output")

# Fungsi ada input, tanpa output
def fungsi2(input1, input2, input3):
    # setiap input argumen hanya dapat di baca di fungsinya sendiri
    print("fungsi2 ini adalah fungsi dengan tiga input, tanpa output")
    print(input1)
    print(input2)
    print(input3)

# fungsi tidak ada input, ada output
def fungsi3():
    print("fungsi3 ini adalah fungsi tanpa input, dengan tiga output")
    output1 = 100
    output2 = 200
    output3 = 300

    return output1, output2, output3

# fungsi ada input dan ada output
def fungsi4(input1, input2):
    print("fungsi4 ini adalah fungsi dengan 2 input dan 2 output")
    output1 = input1 + input2
    output2 = input1 - input2

    return output1, output2

def main():
    fungsi1()
    fungsi2(10, 20, 30)
    a, b, c = fungsi3()
    print(a, b, c)
    x, y = fungsi4(100, 200)
    print(x, y)


if __name__ == "__main__":
    main() # fungsi main adalah fungsi utama