def get_word_count(book_text):
    # This function counts the number of words in the book text.
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    # this function counts the number of times each character appears in the string.
    lower = book_text.lower()
    chars_counts = {}

    for i in lower:
      
        if i in chars_counts:
            #add to the total
            chars_counts[i] += 1
        else:
            #capture the letter
            chars_counts[i] = 1
    return chars_counts

def sort_char_count(chars_counts):
    #this function sorts the dictionary and returns a sorted list

    sorted_list = [] #building the list
   
    for char, count in chars_counts.items():
        if char in "abcdefghijklmnopqrstuvwxyz":
         sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=lambda x: x["num"]) #sorting the list

    return sorted_list
 
    
    

