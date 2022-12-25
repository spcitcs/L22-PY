A = [
    [0,5,6,-2],
    [4,-1,9,0],
    [8,2,-2,8],
    [7,-3,4,3]
]

# 00 11 22 33
# 01 12 23 30
# 02 13 20 31
# 03 10 21 32

# 30 21 12 03
# 31 22 13 00
# 32 23 10 01
# 33 20 11 02

def ks(m:list, dim:int, inv:bool=False) -> float:
    out:float = 0
    for i in range(dim):
        val:float=1
        for j in range(dim):
            x = dim - j - 1 if inv else j
            y = j + i
            y = y - dim if y >= dim else y
            val *= m[x][y]
            print(x,y)
        out += val
    return out



def det(m:list) -> float:
    dim = len(m)
    return ks(m, dim) - ks(m, dim, True)

if __name__ == "__main__":
    print(det(A))