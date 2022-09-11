#Overlap Graphs
import re

def FASTA_to_dict(string):
    dict = {}
    x = re.split('>', string)
    x.remove('')
    for i in x:
        FASTA_unprocessed = re.split('(Rosalind_[0-9]*)', i)
        dict[FASTA_unprocessed[2].strip()] = FASTA_unprocessed[1]
    return dict

f = open("rosalind_grph.txt", "r")
input = f.read()

FASTA_dict = FASTA_to_dict(input)
DNA_strings = list(FASTA_dict.keys())
adjacency = []
# creating the O3 adjacency list
for i in range(len(DNA_strings)):
    for j in range(len(DNA_strings)):
        if (DNA_strings[i][-3:] == DNA_strings[j][:3]) and (DNA_strings[i] != DNA_strings[j]):
            adjacency.append([FASTA_dict[DNA_strings[i]], FASTA_dict[DNA_strings[j]]])



for i in adjacency:
    print(i[0], i[1])
