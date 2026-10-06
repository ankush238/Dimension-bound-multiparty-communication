import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0,1,2], repeat=length))
    return combinations

sequence_length = 3
all_combinations = generate_all_combinations(sequence_length)

combination_matrix_2 = []
for combination in all_combinations:
    combination_matrix_2.append(list(combination))



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
    combinations = list(itertools.product([0, 1, 2], repeat=length))
    return combinations

sequence_length = 9
all_combinations = generate_all_combinations(sequence_length)

alice_combination_matrix_2 = []
for combination in all_combinations:
    alice_combination_matrix_2.append(list(combination))

alice_combination_matrix_2

list_1_decode=[0,1,2]
list_2_decode=[0,1,2]
decoder_2_condition_matrix = list(itertools.product(list_1_decode, list_2_decode))
decoder_2_condition_matrix

def Alice_decoder_2(bob_output, alice_combination_matrix_2, decoder_2_condition_matrix):
    D={}
    
   
    for j in range(len(bob_output)):
        
        for m in range(len(alice_combination_matrix_2)):
            decoded_values = []



            for k in range(len(bob_output[0])):

                for i in range(len(combination_matrix_2[0])):

                    result = (bob_output[j][k][1], i)
                    result_index = decoder_2_condition_matrix.index(result) 
                   
                    decoded_values.append(((bob_output[j][k], i), alice_combination_matrix_2[m][result_index]))
                   
            D[j*(len(alice_combination_matrix_2))+m] = decoded_values
                
                
    
        
    return D

alice_output = Alice_decoder_2(bob_output, alice_combination_matrix_2, decoder_2_condition_matrix)
alice_output

len(alice_output) # 531441

import itertools

def generate_all_combinations(length):
    combinations = list(itertools.product([0, 1], repeat=length))
    return combinations

sequence_length = 3
all_combinations = generate_all_combinations(sequence_length)

charlie_decoding_matrix_2 = []
for combination in all_combinations:
    charlie_decoding_matrix_2.append(list(combination))

charlie_decoding_matrix_2

party_3_input = [0,1,2]


def charlie_decode_3(alice_output_3, charlie_decoding_matrix_3):
    C = {}

    for j in range(len(alice_output_3)):
        for i in range(len(charlie_decoding_matrix_3)):
            decoding_values = []

            for k in range(len(alice_output_3[0])):
                for z in range(len(party_3_input)):
                

                    n = alice_output_3[j][k][1]

                    decoding_values.append(
                        (
                            (alice_output_3[j][k][0][0][0],
                            alice_output_3[j][k][0][1], party_3_input[z]),
                            charlie_decoding_matrix_3[i][n]
                        )
                    )

            C[((i * (len(alice_output_3))) + j)] = decoding_values    # You need to assign a value to this dictionary key

    return C

charlie_output_3 = charlie_decode_3(alice_output, charlie_decoding_matrix_2) 
charlie_output_3

def prob_points_1(output_1):
    N = {}
    for i in range(len(output_1)):
        M = []
        for j in range(len(output_1[0])):
            if output_1[i][j][1]==0:
                prob = 1
            else:
                prob = 0
            M.append(prob)
        N[i]= M
    N = list(N.values())
    return N



extremal_points = prob_points_1(charlie_output_3)
len(extremal_points)
import numpy as np
# Specify the filename for saving the data
filename = "6_dimension_system-6.npy"

# Save the data into a NumPy array file
np.save(filename, extremal_points)

import numpy as np
extremal_points1=np.load("C:\\Users\\PC\\Downloads\\6_dimension_system-6.npy")

unique_rows = np.unique(arr, axis=0)
print(unique_rows)

# Alice remain same but exchange the position between bob and charlie
ext_6_newACB=np.copy(ext_points)
ext_6_new1=np.copy(ext_points)

for i in range(3):
    for j in range(3):
        for k in range(3):
            ext_6_newACB[:,[i*9+j*3+k,i*9+k*3+j]]=ext_6_new1[:,[i*9+k*3+j,i*9+j*3+k]]
            
import numpy as np
from numba import njit
from tqdm import tqdm  # Progress tracking

# Example Data (Replace with actual data)
list1 = ext_points # Simulating ext8_new2
list2 = ext_6_newACB  # Simulating A2

# Ensure the data is NumPy arrays
list1 = np.array(list1)
list2 = np.array(list2)

# Numba JIT function for fast row checking
@njit
def check_rows(list2_chunk, list1):
    mask = np.zeros(len(list2_chunk), dtype=np.bool_)  # Boolean mask
    for i in range(len(list2_chunk)):
        for row in list1:
            if np.array_equal(list2_chunk[i], row):  # Check if row exists
                mask[i] = False
                break
        else:
            mask[i] = True  # Mark as unequal
    return mask

# Chunk processing with tqdm
chunk_size = max(1, len(list2) // 100)  # Adjust chunk size (~100 updates)
mask_list = np.zeros(len(list2), dtype=np.bool_)  # Global mask

for i in tqdm(range(0, len(list2), chunk_size), desc="Checking Progress"):
    chunk_indices = slice(i, i + chunk_size)  # Define chunk indices
    mask_list[chunk_indices] = check_rows(list2[chunk_indices], list1)  # Compute mask

# Extract rows that are in list2 but not in list1
unequal_rows1 = list2[mask_list]  # ✅ Corrected indexing

# Print results
print("Unequal rows (present in list2 but not in list1):")
print(unequal_rows1)

# Alice remain same but exchange the position between bob and charlie
ext_6_newCBA=np.copy(ext_points)
ext_6_new1=np.copy(ext_points)

for i in range(3):
    for j in range(3):
        for k in range(3):
            ext_6_newCBA[:,[i*9+j*3+k,i+j*3+k*9]]=ext_6_new1[:,[i+j*3+k*9,i*9+j*3+k]]
            
import numpy as np
from numba import njit
from tqdm import tqdm  # Progress tracking

# Example Data (Replace with actual data)
list1 = ext_points # Simulating ext8_new2
list2 = ext_6_newCBA  # Simulating A2

# Ensure the data is NumPy arrays
list1 = np.array(list1)
list2 = np.array(list2)

# Numba JIT function for fast row checking
@njit
def check_rows(list2_chunk, list1):
    mask = np.zeros(len(list2_chunk), dtype=np.bool_)  # Boolean mask
    for i in range(len(list2_chunk)):
        for row in list1:
            if np.array_equal(list2_chunk[i], row):  # Check if row exists
                mask[i] = False
                break
        else:
            mask[i] = True  # Mark as unequal
    return mask

# Chunk processing with tqdm
chunk_size = max(1, len(list2) // 100)  # Adjust chunk size (~100 updates)
mask_list = np.zeros(len(list2), dtype=np.bool_)  # Global mask

for i in tqdm(range(0, len(list2), chunk_size), desc="Checking Progress"):
    chunk_indices = slice(i, i + chunk_size)  # Define chunk indices
    mask_list[chunk_indices] = check_rows(list2[chunk_indices], list1)  # Compute mask

# Extract rows that are in list2 but not in list1
unequal_rows2 = list2[mask_list]  # ✅ Corrected indexing

# Print results
print("Unequal rows (present in list2 but not in list1):")
print(unequal_rows2)

# Alice remain same but exchange the position between bob and charlie
ext_6_newBAC=np.copy(ext_points)
ext_6_new1=np.copy(ext_points)

for i in range(3):
    for j in range(3):
        for k in range(3):
            ext_6_newBAC[:,[i*9+j*3+k,i*3+j*9+k]]=ext_6_new1[:,[i*3+j*9+k,i*9+j*3+k]]
            
import numpy as np
from numba import njit
from tqdm import tqdm  # Progress tracking

# Example Data (Replace with actual data)
list1 = ext_points # Simulating ext8_new2
list2 = ext_6_newBAC  # Simulating A2

# Ensure the data is NumPy arrays
list1 = np.array(list1)
list2 = np.array(list2)

# Numba JIT function for fast row checking
@njit
def check_rows(list2_chunk, list1):
    mask = np.zeros(len(list2_chunk), dtype=np.bool_)  # Boolean mask
    for i in range(len(list2_chunk)):
        for row in list1:
            if np.array_equal(list2_chunk[i], row):  # Check if row exists
                mask[i] = False
                break
        else:
            mask[i] = True  # Mark as unequal
    return mask

# Chunk processing with tqdm
chunk_size = max(1, len(list2) // 100)  # Adjust chunk size (~100 updates)
mask_list = np.zeros(len(list2), dtype=np.bool_)  # Global mask

for i in tqdm(range(0, len(list2), chunk_size), desc="Checking Progress"):
    chunk_indices = slice(i, i + chunk_size)  # Define chunk indices
    mask_list[chunk_indices] = check_rows(list2[chunk_indices], list1)  # Compute mask

# Extract rows that are in list2 but not in list1
unequal_rows3 = list2[mask_list]  # ✅ Corrected indexing

# Print results
print("Unequal rows (present in list2 but not in list1):")
print(unequal_rows3)

# BAC to BCA
ext_6_newBCA=np.copy(ext_6_newBAC)
ext_6_new1=np.copy(ext_6_newBAC)

for i in range(3):
    for j in range(3):
        for k in range(3):
            ext_6_newBCA[:,[i*9+j*3+k,i*9+j+k*3]]=ext_6_new1[:,[i*9+j+k*3,i*9+j*3+k]]
            
import numpy as np
from numba import njit
from tqdm import tqdm  # Progress tracking

# Example Data (Replace with actual data)
list1 = ext_points # Simulating ext8_new2
list2 = ext_6_newBCA  # Simulating A2

# Ensure the data is NumPy arrays
list1 = np.array(list1)
list2 = np.array(list2)

# Numba JIT function for fast row checking
@njit
def check_rows(list2_chunk, list1):
    mask = np.zeros(len(list2_chunk), dtype=np.bool_)  # Boolean mask
    for i in range(len(list2_chunk)):
        for row in list1:
            if np.array_equal(list2_chunk[i], row):  # Check if row exists
                mask[i] = False
                break
        else:
            mask[i] = True  # Mark as unequal
    return mask

# Chunk processing with tqdm
chunk_size = max(1, len(list2) // 100)  # Adjust chunk size (~100 updates)
mask_list = np.zeros(len(list2), dtype=np.bool_)  # Global mask

for i in tqdm(range(0, len(list2), chunk_size), desc="Checking Progress"):
    chunk_indices = slice(i, i + chunk_size)  # Define chunk indices
    mask_list[chunk_indices] = check_rows(list2[chunk_indices], list1)  # Compute mask

# Extract rows that are in list2 but not in list1
unequal_rows4 = list2[mask_list]  # ✅ Corrected indexing

# Print results
print("Unequal rows (present in list2 but not in list1):")
print(unequal_rows4)

# Alice remain same but exchange the position between bob and charlie
ext_6_newCAB=np.copy(ext_6_newCBA)
ext_6_new1=np.copy(ext_6_newCBA)

for i in range(3):
    for j in range(3):
        for k in range(3):
            ext_6_newCAB[:,[i*9+j*3+k,i*9+k*3+j]]=ext_6_new1[:,[i*9+k*3+j,i*9+j*3+k]]
            
import numpy as np
from numba import njit
from tqdm import tqdm  # Progress tracking

# Example Data (Replace with actual data)
list1 = ext_points # Simulating ext8_new2
list2 = ext_6_newCAB  # Simulating A2

# Ensure the data is NumPy arrays
list1 = np.array(list1)
list2 = np.array(list2)

# Numba JIT function for fast row checking
@njit
def check_rows(list2_chunk, list1):
    mask = np.zeros(len(list2_chunk), dtype=np.bool_)  # Boolean mask
    for i in range(len(list2_chunk)):
        for row in list1:
            if np.array_equal(list2_chunk[i], row):  # Check if row exists
                mask[i] = False
                break
        else:
            mask[i] = True  # Mark as unequal
    return mask

# Chunk processing with tqdm
chunk_size = max(1, len(list2) // 100)  # Adjust chunk size (~100 updates)
mask_list = np.zeros(len(list2), dtype=np.bool_)  # Global mask

for i in tqdm(range(0, len(list2), chunk_size), desc="Checking Progress"):
    chunk_indices = slice(i, i + chunk_size)  # Define chunk indices
    mask_list[chunk_indices] = check_rows(list2[chunk_indices], list1)  # Compute mask

# Extract rows that are in list2 but not in list1
unequal_rows5 = list2[mask_list]  # ✅ Corrected indexing

# Print results
print("Unequal rows (present in list2 but not in list1):")
print(unequal_rows5)

len(unequal_rows2)

a1to2toreceiver33=np.vstack((unequal_rows1,unequal_rows2,unequal_rows3,unequal_rows4,unequal_rows5))
np.save('a1to2toreceiver33',a1to2toreceiver33)
