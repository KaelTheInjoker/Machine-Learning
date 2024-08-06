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

user_input = input('Pls input sthing:')



# def check_input():
#     length = len(user_input)
    
    





































