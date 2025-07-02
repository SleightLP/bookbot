import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def get_book_text(book):
   # This function reads the content of a book file and returns it as a string.
    with open(book) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    character_count = get_char_count(book_text)
    sorted = sort_char_count(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
   # print(f"{character_count}")
   # print(f"{sorted}")
    for item in sorted:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()