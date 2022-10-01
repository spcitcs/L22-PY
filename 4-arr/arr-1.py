# Basic Array
# import os


# os.system("clear")
# List
arr =  [1,2,3,4,5,6,7,8,"Alfian",9,True]

print(arr[1])
print(arr[0])
print(arr[8])
print(arr[-3])
print(arr[-11])
# print(arr[11]) # ERROR!
# print(arr[-12]) # ERROR

# Len Function dan Index
# Cara menentukan panjang array python
panjangArray = len(arr)
print(panjangArray) # 10/11

arr1 = [1, "A", 2, "B", 3, "C", 4, "D"]
arr2 = ["A", "B", "A", "C", 1,2,3,5,]

print(arr1) # [1, 'A', 2, 'B', 3, 'C', 4, 'D']
print(arr2[1]) # B
# print(arr1[10]) # Err
print(arr2[-3]) # 2
print(arr1[2**2]) # 3
print(arr2[int(3-(4/2))]) # B
print(arr1[int("12") - 10]) # 2 
print(arr2[-6]) # A
# print(arr1[str(-2)]) # Err 
print(arr2) # ['A','B','A','C',1,2,3,5]
print(len(arr1)) # 8
print(len(arr2) * 2) # 16

# Sub List
arr = [1,2,3,4,5,6,7,8,9,10]

print(arr[:5:1]) 
print(arr[:5:-1])
print(arr[5::-1])
print(arr[5::1])

fruits = ["apel", "mangga", "anggur", "jeruk", "markisa"]

print(arr[1:5:2]) # [2,4]
print(fruits[2::-1]) # ["mangga", "apel"]
print(arr[3::3]) # [4,7,10] [4,7]
print(fruits[:5:-2]) # [] 
print(arr[-2:-5:-2]) # [9,7]
print(fruits[-1:]) # ["Durian"]
print(arr[7]) # 8
print(fruits[0:]) # semua
print(arr[3:-3:]) # [4,5,6,7]
print(fruits[::]) # semua
print(arr[len(fruits):len(fruits[:-2])*-1])
# [6,7]

print(arr[0:11:1]) # [1,2,3,4,5,6,7,8,9,10]
print(arr[::2]) # [2,4,6,8,10]
print(fruits[::3]) # jeruk, anggur

print(len(arr)) # 10
print(arr[5]) # 6
print(arr[9]) # 10
print(arr[5:9]) # [6,7,8,9]
print(arr[5:10]) # [6,7,8,9,10]
# print(arr[10]) # Index Out of Range
print(arr[5:-2]) # [6, 7, 8]
print(arr[-5:-2]) # [6, 7, 8]
print(arr[2:5]) # [3,4,5]
print(arr[5:2]) # [5,4,3] 
print(arr[5:-3]) # [6, 7] 
print(arr[5:-6]) # []
print(arr[5:]) # [6,7,8,9,10]
print(arr[:5]) # [1,2,3,4,5]
print(arr[:-8]) # [1,2]
print(arr[-8:]) # [3,4,5,6,7,8,9,10]
print(arr[:])

# Append
# Remove
# Sort