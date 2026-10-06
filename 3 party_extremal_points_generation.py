import itertools
import numpy as np
def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 3
all_combinations = generate_all_combinations(sequence_length)

combination_matrix_1 = []
for combination in all_combinations:
    
    combination_matrix_1.append(list(combination))

combination_matrix_1

combination_matrix_1= np.array( combination_matrix_1)

def Alice_encode_1(combination_matrix_1):
    E = {}
    for i in range (len(combination_matrix_1)):
        encoded_values = []
        for j in range (len(combination_matrix_1[0])):
            encoded_values.append( (j,combination_matrix_1[i,j]))
            E[i] = encoded_values
    return E
Alice_output_1 = Alice_encode_1(combination_matrix_1)

Alice_output_1

result = {
    k: [(i, int(val)) for i, val in v]
    for k, v in Alice_output_1.items()}
result

def Bob_encode_1(combination_matrix_1):
    E = {}
    for i in range (len(combination_matrix_1)):
        encoded_values = []
        for j in range (len(combination_matrix_1[0])):
            encoded_values.append((j,combination_matrix_1[i,j]))
            E[i] = encoded_values
    return E

Bob_output_1 =Bob_encode_1(combination_matrix_1)


result = {
    k: [(i, int(val)) for i, val in v]
    for k, v in Bob_output_1.items()}
result


def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 4
all_combinations = generate_all_combinations(sequence_length)

charlie_matrix_1 = []
for combination in all_combinations:
    
    charlie_matrix_1.append(list(combination))

charlie_matrix_1

def charlie_decode_1(Alice_output_1,Bob_output_1,charlie_matrix_1):
    D={}
    
    for i in range(len(Alice_output_1)):
        
        for j in range(len(Bob_output_1)):
            
            for k in range(len(charlie_matrix_1)):
                decode_values = []
                
                for p in range(len(Alice_output_1[0])):
                    
                    for m in range(len(Bob_output_1[0])):
                        
                        if (Alice_output_1[i][p][1], Bob_output_1[j][m][1]) == (0, 0):
                            n = 0
                        if (Alice_output_1[i][p][1], Bob_output_1[j][m][1]) == (0, 1):
                            n = 1
                        if (Alice_output_1[i][p][1], Bob_output_1[j][m][1]) == (1, 0):
                            n = 2
                        if (Alice_output_1[i][p][1], Bob_output_1[j][m][1]) == (1, 1):
                            n = 3
                        decode_values.append(((Alice_output_1[i][p][0], Bob_output_1[j][m][0]),charlie_matrix_1[k][n]))
                D[(i * (len(Alice_output_1)) * (len(charlie_matrix_1))) + (j * len(charlie_matrix_1)) +k] = decode_values
    
    return D

charlie_output_1 = charlie_decode_1(Alice_output_1,Bob_output_1,charlie_matrix_1)
len(charlie_output_1)


charlie_output_1

extremal_points ={}
for i in range(len(charlie_output_1)):
    p = []
    for j in range(len(charlie_output_1[0])):
        p.append(charlie_output_1[i][j][1])
        extremal_points[i]=p

extremal_points

ext_points =list(extremal_points.values())
ext_points = np.array(ext_points)
print(ext_points)


def calculate_output(input_dict):
    output_dict = {}
    for i in range(len(input_dict)):
        p=[]
        for j in range(len(input_dict[1])):
            # Count the number of zeros in the value
            num_zeros = input_dict[i].count(0)

            # Calculate the output based on the condition
            if input_dict[i][j]==0:
                output = 1 
            else:
                output = 0
            p.append(output)

            # Store the output in the output dictionary
        output_dict[i] = p

    return output_dict


extremal_prob_points = calculate_output(extremal_points)

print(extremal_prob_points )


extremal_prob_points = list(extremal_prob_points.values())
print(extremal_prob_points )

extremal_prob_points =np.array(extremal_prob_points)
print(extremal_prob_points )
print(len(ext_points))
ext_copy_1=np.copy(ext_points)
ext_copy_1[:,[1,3]]=ext_copy_1[:,[3,1]]
ext_copy_1[:,[2,6]]=ext_copy_1[:,[6,2]]
ext_copy_1[:,[5,7]]=ext_copy_1[:,[7,5]]
result=[]
for row in ext_copy_1:
    found = False
    for b_row in ext_points:
        if np.array_equal(row, b_row):
            found = True
            break

    if not found:
        result.append(row)

result = np.array(result)
print(result)
np.save('extremal_prob_points_1.npy', ext_points)

# Alice to Bob to Charlie

import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0,1], repeat=length))
    return combinations

sequence_length = 3
all_combinations = generate_all_combinations(sequence_length)

combination_matrix_2 = []
for combination in all_combinations:
    combination_matrix_2.append(list(combination))

combination_matrix_2


def Bob_encode_2(combination_matrix_2):
    E = {}
    for i in range (len(combination_matrix_2)):
        encoded_values = []
        for j in range (len(combination_matrix_2[0])):
            encoded_values.append((j,combination_matrix_2[i][j]))
            E[i] = encoded_values
    return E

bob_output = Bob_encode_2(combination_matrix_2)

bob_output


import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 6
all_combinations = generate_all_combinations(sequence_length)

alice_combination_matrix_2 = []
for combination in all_combinations:
    alice_combination_matrix_2.append(list(combination))

alice_combination_matrix_2

def Alice_decoder_2(bob_output, alice_combination_matrix_2):
    D={}
    
   
    for j in range(len(bob_output)):
        
        for m in range(len(alice_combination_matrix_2)):
            decoded_values = []



            for k in range(len(bob_output[0])):

                for i in range(len(combination_matrix_2[0])):

                    if (bob_output[j][k][1], i) == (0,0):
                        n = 0
                    if (bob_output[j][k][1], i) == (1,0):
                        n = 1
                    if (bob_output[j][k][1], i) == (0,1):
                        n = 2
                    if (bob_output[j][k][1], i) == (1, 1):
                        n = 3
                    if (bob_output[j][k][1], i) == (0,2):
                        n = 4
                    if (bob_output[j][k][1], i) == (1,2):
                        n = 5
                   

                    decoded_values.append(((bob_output[j][k], i), alice_combination_matrix_2[m][n]))
                   
            D[j*(len(alice_combination_matrix_2))+m] = decoded_values
                
                
    
    return D

alice_output =  Alice_decoder_2(bob_output, alice_combination_matrix_2)

alice_output

len(alice_output)


import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 2
all_combinations = generate_all_combinations(sequence_length)

charlie_decoding_matrix_2 = []
for combination in all_combinations:
    charlie_decoding_matrix_2.append(list(combination))

charlie_decoding_matrix_2

def charlie_decode_3(alice_output_3, charlie_decoding_matrix_3):
    C = {}

    for i in range(len(charlie_decoding_matrix_3)):
        for j in range(len(alice_output_3)):
            decoding_values = []

            for k in range(len(alice_output_3[0])):
                

                if alice_output_3[j][k][1] == 0:
                    n = 0
                if alice_output_3[j][k][1] == 1:
                    n = 1 

                decoding_values.append(
                    (
                        (alice_output_3[j][k][0][0][0],
                         alice_output_3[j][k][0][1]),
                        charlie_decoding_matrix_3[i][n]
                    )
                )

            C[((i * (len(alice_output))) + j)] = decoding_values    # You need to assign a value to this dictionary key

    return C


charlie_output_3 = charlie_decode_3(alice_output, charlie_decoding_matrix_2)
print(charlie_output_3)

extremal_points_2 ={}
for i in range(len(charlie_output_3)):
    p = []
    for j in range(len(charlie_output_3[0])):
        p.append(charlie_output_3[i][j][1])
        extremal_points_2[i]=p
ext_points_2 =list(extremal_points_2.values())
ext_points_2 = np.array(ext_points_2)
print(len(ext_points_2))

ext_points_2


np.save('extremal_prob_points_2.npy', ext_points_2)


ext_copy_2 = np.copy(ext_points_2)
ext_copy_2[:,[1,3]]=ext_copy_2[:,[3,1]]
ext_copy_2[:,[2,6]]=ext_copy_2[:,[6,2]]
ext_copy_2[:,[5,7]]=ext_copy_2[:,[7,5]]


result=[]
for row in ext_copy_2:
    found = False
    for b_row in ext_points_2:
        if np.array_equal(row, b_row):
            found = True
            break

    if not found:
        result.append(row)

result = np.array(result)
print(result)

np.save('extremal_prob_points_3.npy', result) # EXTRA EXTREMAL POINTS


len(result) # 288

# Alice to Charlie

import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0,1,2,3], repeat=length))
    return combinations

sequence_length = 3
all_combinations = generate_all_combinations(sequence_length)

combination_matrix_3 = []
for combination in all_combinations:
    combination_matrix_3.append(list(combination))

combination_matrix_3

def Alice_encode_2(combination_matrix_3):
    E = {}
    for i in range (len(combination_matrix_3)):
        encoded_values = []
        for j in range (len(combination_matrix_3[0])):
            encoded_values.append((j,combination_matrix_3[i][j]))
            E[i] = encoded_values
    return E

Alice_output = Alice_encode_2(combination_matrix_3)
Alice_output

import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 4
all_combinations = generate_all_combinations(sequence_length)

charlie_decoding_matrix_2 = []
for combination in all_combinations:
    charlie_decoding_matrix_2.append(list(combination))

charlie_decoding_matrix_2

party_3_input = [0,1,2]


def charlie_decode_3(alice_output_3, charlie_decoding_matrix_3):
    C = {}

    for i in range(len(charlie_decoding_matrix_3)):
        for j in range(len(alice_output_3)):
            decoding_values = []

            for k in range(len(alice_output_3[0])):
                for z in range(len(party_3_input)):
                

                    n = alice_output_3[j][k][1]

                    decoding_values.append(
                        (
                            (alice_output_3[j][k][0],
                            party_3_input[z]),
                            charlie_decoding_matrix_3[i][n]
                        )
                    )

            C[((i * (len(alice_output_3))) + j)] = decoding_values    # You need to assign a value to this dictionary key

    return C

charlie_output_3 = charlie_decode_3(Alice_output, charlie_decoding_matrix_2)

charlie_output_3

extremal_points_3 ={}
for i in range(len(charlie_output_3)):
    p = []
    for j in range(len(charlie_output_3[0])):
        p.append(charlie_output_3[i][j][1])
        extremal_points_3[i]=p


extremal_points_3

len(extremal_points_3)

def calculate_output_2(input_dict):
    output_dict = {}
    for i in range(len(input_dict)):
        p=[]
        for j in range(len(input_dict[1])):
            # Count the number of zeros in the value
            num_zeros = input_dict[i].count(0)

            # Calculate the output based on the condition
            if input_dict[i][j]==0:
                output = 1 
            else:
                output = 0
            p.append(output)

            # Store the output in the output dictionary
        output_dict[i] = p

    return output_dict

extremal_prob_points_3 = calculate_output_2(extremal_points_3)

extremal_prob_points_3 = list(extremal_prob_points_3.values())
extremal_prob_points_3 =np.array(extremal_prob_points_3)
print(extremal_prob_points_3 )

np.save('extremal_prob_points_4.npy', extremal_prob_points_3)

ext_copy_3=np.copy(all_points)

ext_copy_3[:,[1,3]]=ext_copy_3[:,[3,1]]
ext_copy_3[:,[2,6]]=ext_copy_3[:,[6,2]]
ext_copy_3[:,[5,7]]=ext_copy_3[:,[7,5]]
result3=[]
for row in ext_copy_3:
    found = False
    for b_row in all_points:
        if np.array_equal(row, b_row):
            found = True
            break

    if not found:
        result3.append(row)

result = np.array(result3)
print(result3)

len(result3)

all_points = list(extremal_points_3.values())
all_points

np.save('extremal_prob_points_5.npy', result3)

import numpy as np
a=np.load('/home/c_01/Desktop/extremal_prob_points_5.npy')
b=np.load('/home/c_01/Desktop/extremal_prob_points_4.npy')
c=np.load('/home/c_01/Desktop/extremal_prob_points_3.npy')
d=np.load('/home/c_01/Desktop/extremal_prob_points_2.npy')
#e=np.load('/home/c_01/Desktop/extremal_prob_points_1.npy')

all_extremal_points=np.unique(all_extremal_points, axis=0)

len(all_extremal_points)

V=np.vectorize(lambda x: str(Fraction(x).limit_denominator()))(all_extremal_points)
for row in V:
    print(" ".join(row))
