#Calculating Expected Offspring

#AA-AA - 1
#AA-Aa - 1
#AA-aa - 1
#Aa-Aa - 75%
#Aa-aa - 50%
#aa-aa - 0 %

f = open("rosalind_iev.txt", "r")
input = f.read().split()
prob = [1, 1, 1, 0.75, 0.5, 0]

expected_value = 0
for i in range(6):
    expected_value += prob[i]*int(input[i])
print(expected_value*2)
