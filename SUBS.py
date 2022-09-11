import re

#find first index loc for all substrings
def find_substrings(func_string):
    loc = func_string.find(substring)
    if loc == -1:
        return
    else:
        shortened_by = len(string) - len(func_string)
        locations.append(str(loc + 1 + shortened_by))
        find_substrings(func_string[loc + 1:])
        return

#open file
f = open("rosalind_subs.txt", "r")
input = f.read().splitlines()
string = input[0]
substring = input[1]
locations = []

find_substrings(string)

print(" ".join(locations))

