# Oliver Smith 
# Binary Search

import time

# imports file
list_file = open("words.txt","r")

# create array from words
list = []
for line in list_file:
     list.append(line[:-1]) # removes the '\n' at the end of each item before appending
     


# Binary Search Alg
def binary_search(list, search_word,current_index,min_pointer,max_pointer): # min_pointer and max_pointer mark the bounds of the subarray
                                                                            # current_index points to the midpoint of the subarray
                                                          
    # word not found end condition 
    if min_pointer > max_pointer:
        return -1

    current_word = list[current_index] # Word at the midpoint of the subarray
    
    # uncomment to display iterations
    # print(current_word, current_index, min_pointer, max_pointer)
    # time.sleep(0.05)
    

    # found word end case
    if current_word == search_word:
        return current_index

    # recursive loop
    else:
        
        if search_word < current_word: # compares position in alphabet
            return binary_search(list,search_word,(min_pointer + current_index-1)//2, min_pointer, current_index-1)
        else:
            return binary_search(list,search_word,(current_index+1 + max_pointer)//2,current_index+1,max_pointer)
    



while True: # Infinite loop
   
    word_to_find = str(input("What word do you want to find in the list?: ")) # user input

    search_result = binary_search(list, word_to_find,len(list)//2,0,len(list)) # Stores result from binary_search() function

    if search_result >= 0: # Function returns index if word is found
        print("That word is in the list at line",search_result+1)
    else:
        print("That word is not in the list.")



