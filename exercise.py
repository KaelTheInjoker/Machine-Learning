#==================================CURRENT=======================#


# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np 

ex1_2 = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]

def numpy_sort():
    arr = np.array(ex1_2)
    reverse_arr = arr[::-1] 
    return print(reverse_arr)

# numpy_sort()

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

arr_1 = [0,10,20,40,60]
arr_2 = [10, 30, 40]

def numpy_check():
    arr_1_1 = np.array(arr_1)
    arr_2_1 = np.array(arr_2)
    check = np.isin(arr_1_1,arr_2_1)
    return print(check)

# numpy_check()



# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]g

def check_numpy_3():
    arr = np.array([1,6,4,8,9,-4,-2,11])
    max_val = np.max(arr)
    min_val = np.min(arr)
    out_put = []
    for i in range(len(arr)):
        if arr[i] == min_val:
            out_put.append(i)
        if arr[i] == max_val:
            out_put.append(i)
    return print(out_put)

# check_numpy_3()

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

import pandas as pd

# file = pd.read_csv('abc.txt')

# file = pd.read_txt('D:\Development\Data Projects (SQL & Python)\Python\Machine Learning\story.txt', delimiter='\t', header=0)
with open('D:\Development\Data Projects (SQL & Python)\Python\Machine Learning\story.txt', 'r') as f:
    text = f.read()
    
words = pd.Series(text.split())
word_cnt = words.value_counts()
df = pd.DataFrame(word_cnt, columns=['word_cnt']).sort_values(['word_cnt'], ascending = False)

print(df.head(100))




#==========OLD===========


# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]


def count_pos_neg():
    pos_list = [] 
    neg_list = []
    for i in data1:
        if i < 0:
            neg_list.append(i) 
        else:
            pos_list.append(i)
    return print('positive_cnt: {}, negative_cnt: {}'.format(len(pos_list), len(neg_list)))

# count_pos_neg()


# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def check_feq():
    final_list = []
    for i in data2:
        if data2.count(i) >= k:
            final_list.append(i) 
    return print(final_list)

# check_feq()


# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]


# =============================================================================
# def check_max():
#     print(sorted(data3)[len(data3) - 1]) #index start from 0, hence have to deduct by 1
#             
# check_max()
# =============================================================================


def check_max2():
    output_list = []
    for i in data3:
        for j in range(0, len(data3)):
            if j == data3.index(i) + 1 and i < data3[j]:
                output_list.append(data3[j])
            elif j == data3.index(i) + 1 and i > data3[j]:
                output_list.append(i)
    return print(output_list)

# check_max2()


# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

def combination():
    for i in data4:
        for j in data4:
            for z in data4:
                print('{}{}{}'.format(i,j,z))

# combination()



# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]


def list_join():
    output_list=data5_list1
    for i in range(0, len(data5_list1)):
        for j in range(0, len(data5_list2)):
            if i == j:
                for z in range(0, len(data5_list2[j])):   
                    output_list[i].append(data5_list2[j][z])
    return print(output_list)

# list_join()





# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def div_7_not_mul_5():
    output=[]
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            output.append(i)
    return print(output)

# div_7_not_mul_5()





# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def find_even():
    output=[]
    for i in range(1000, 3001):
        if i % 2 == 0:
            output.append(i)
    return print(output)

# find_even()





# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

# user_input = input('Pls input 2 random words in English:')
# print(user_input)

# def word_check():
#     list_of_words = user_input.split()
#     len_check = []
    
#     for i in list_of_words:
#         if len(i) >= 3:
#             len_check.append(True) 
#         else:
#             len_check.append(False) 
            
    


# def check_input():
#     length = len(user_input)
    
    



















