#Mortal Fibonacci Rabbits

def modified_fib(func_n, death_m):
    #base case
    if func_n in {0, 1}:
        return func_n
    #normal, no death version
    elif func_n <= death_m:
        return modified_fib(func_n - 1, death_m) + modified_fib(func_n - 2,  death_m)
    #death occurs
    elif func_n == death_m + 1:
        return modified_fib(func_n - 1, death_m) + modified_fib(func_n - 2,  death_m) - 1
    else:
        return modified_fib(func_n - 1, death_m) + modified_fib(func_n - 2,  death_m) - modified_fib(func_n - (death_m + 1), death_m)

#open files
f = open("rosalind_fibd.txt", "r")
input = f.read().split()
n = int(input[0])
m = int(input[1])

print(modified_fib(n, m))
