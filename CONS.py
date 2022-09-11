#	Consensus and Profile

import re

#open files
f = open("rosalind_cons.txt", "r")
input = f.read()
input = re.sub('\n', '', input)
x = re.split('>Rosalind_[0-9]*', input)
x.remove('')
DNA_string_num = len(x)
DNA_length = len(x[0])
profile_matrix = [[], [], [], []]
consensus_string = ''

#forming the profile matrix
for i in range(DNA_length):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for j in range(DNA_string_num):
        if x[j][i] == 'A':
            a_count += 1
        elif x[j][i] == 'C':
            c_count += 1
        elif x[j][i] == 'G':
            g_count += 1
        elif x[j][i] == 'T':
            t_count += 1
    profile_matrix[0].append(str(a_count))
    profile_matrix[1].append(str(c_count))
    profile_matrix[2].append(str(g_count))
    profile_matrix[3].append(str(t_count))

    find_max = max([a_count, c_count, g_count, t_count])
    if a_count == find_max:
        consensus_string += 'A'
    elif c_count == find_max:
        consensus_string += 'C'
    elif g_count == find_max:
        consensus_string += 'G'
    elif t_count == find_max:
        consensus_string += 'T'

#formatting printing
print(consensus_string)
a_print = " ".join(profile_matrix[0])
c_print = " ".join(profile_matrix[1])
g_print = " ".join(profile_matrix[2])
t_print = " ".join(profile_matrix[3])
print('A: ' + a_print + '\nC: '+ c_print + '\nG: '+ g_print + '\nT: '+ t_print)
