#Finding a Shared Motif
import re

def find_substring(DNA_arr):
    arr_size = len(DNA_arr)
    longest_substring = ""

    #taking first string as aribitrary reference - testing all substrings
    for i in range(len(DNA_arr[0])):
        for j in range(i + 1, len(DNA_arr[0]) + 1):

            poss_substring = DNA_arr[0][i:j]

            # test all of these possible substrings
            counter = 0
            for k in range(1, arr_size):
                if poss_substring not in DNA_arr[k]:
                    break
                else:
                    counter += 1

            #find the longest substrings
            if counter + 1 == arr_size and len(longest_substring) < len(poss_substring):
                longest_substring = poss_substring
    return longest_substring


f = open("rosalind_lcsm.txt", "r")
input = f.read()
DNA_strings_unprocessed = re.split('>Rosalind_[0-9]*', input)
DNA_strings_unprocessed.remove('')
DNA_strings = []
for i in DNA_strings_unprocessed:
    DNA_strings.append(i.replace('\n', ''))

print(find_substring(DNA_strings))
