def Permutazioni(n):
    '''Create a function that takes a variable number of arguments, each argument representing the number of items in a group,
       and returns the number of permutations (combinations) of items that you could get by taking one item from each group'''
    perm = 1
    counter = 0
    if len(n)==0:
        perm = 0
    else:
        for i in n:
            if i != 0:
                perm *= i
            else:
                counter += 1
    if len(n) == counter:
        perm = 0
    print(perm)

n=(2,3)
Permutazioni(n)
n=(3,7,4)
Permutazioni(n)
n=(3,7,4,0)
Permutazioni(n)
n=()
Permutazioni(n)
n=(0,0)
Permutazioni(n)