list_size = 4096
li = [None] * list_size # empty list of size 4096. we take [none] instead of [] as it would be a list of size 0

# a hashing algo that can be :
# using ord python inbuilt func to convert a character in a string to a number and adding those numbers in the end . the number can get big so we take remainder using list_size. we get a index for that string

def get_index(list_pass,string_pass):

    result=0 # storing the resultant concatenated num after loop

    for i in string_pass:
        num = ord(i)  # converting each char of string to number
        result+= num

    li_index = result % len(list_pass)
    return li_index
# print(get_index(li,"hi"))        

key,value = 'hi','256'

index = get_index(li,key)
li[index] = (key,value) # insertng the key,value at the index

# print(index)
# print(li[index])

idx = get_index(li,key) # we get the hash/index of key for finding the key-value pair in list
key1 ,value1 = li[idx]

# print(f"{key,value}")

# getting a list of keys
keys = [i[0] for i in li if i is not None] # filtering null keys. i[0] as thats the index of key in a key-value pair
print(keys)