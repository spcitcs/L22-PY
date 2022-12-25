import math

# pangkat genap positif
# pangkat ganjil negatif

def toInteger(val:list[int]) -> int:
    value = 0
    for i in range(len(val)):
        bit = 2 ** i
        value += (bit * (1 if i % 2 == 0 else -1)) * val[i]
    return value

def toBit(val:int) -> list[int]:
    bitValue = []

    i = 1
    while True:
        bitValue.append(0)
        if 2 ** i > val:
            i -= 1
            break
        i += 1
       
    
    for n in range(i, -1, -1):
        newVal = val % (2 ** n)
        if newVal != val:
            bitValue[n] = 1
            val = newVal
            if n % 2 == 1:
                if len(bitValue) <= n + 1:
                    bitValue.append(1)
                else:
                    bitValue[n + 1] = 1

    return bitValue


def solution(A):
   asInteger = toInteger(A)
   divTwo = math.ceil(asInteger/2)
   return toBit(divTwo)


print(solution([1,0,0,1,1,1]))
print(solution([0,0,1,0,1,1]))
print(solution([1,0,0,1,1]))
print(solution([0,0,1]))