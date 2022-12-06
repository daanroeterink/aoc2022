import os
import re

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

#         [H]     [W] [B]            
#     [D] [B]     [L] [G] [N]        
# [P] [J] [T]     [M] [R] [D]        
# [V] [F] [V]     [F] [Z] [B]     [C]
# [Z] [V] [S]     [G] [H] [C] [Q] [R]
# [W] [W] [L] [J] [B] [V] [P] [B] [Z]
# [D] [S] [M] [S] [Z] [W] [J] [T] [G]
# [T] [L] [Z] [R] [C] [Q] [V] [P] [H]
#  1   2   3   4   5   6   7   8   9 

regex = r"move (\d*) from (\d*) to (\d*)"

dict_stack = {}

dict_stack[1] = ['P','V','Z','W','D','T']
dict_stack[2] = ['D','J','F','V','W','S','L']
dict_stack[3] = ['H','B','T','V','S','L','M','Z']
dict_stack[4] = ['J','S','R']
dict_stack[5] = ['W','L','M','F','G','B','Z','C']
dict_stack[6] = ['B','G','R','Z','H','V','W','Q']
dict_stack[7] = ['N','D','B','C','P','J','V']
dict_stack[8] = ['Q','B','T','P']
dict_stack[9] = ['C','R','Z','G','H']

for k in dict_stack:
    dict_stack[k] = dict_stack[k][::-1]


for line in input_lines:
    x = re.search(regex,line)
    amount = int(x.group(1))
    starter = int(x.group(2))
    end = int(x.group(3))

    cratesToAdd = []

    for x in range(amount):
       cratesToAdd += dict_stack[starter].pop()
    
    cratesToAdd = cratesToAdd[::-1]

    for crate in cratesToAdd:
        dict_stack[end].append(crate)



for k in dict_stack:
    print(dict_stack[k][-1])


