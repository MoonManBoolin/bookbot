from stats import get_word_count
from stats import get_char_count
from stats import sort_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    get_word_count(book_text)
    char_count = get_char_count(book_text)
    print("--------- Character Count -------")
    sorted_char_list = sort_list(char_count)
    for obj in sorted_char_list:
        if list(obj.keys())[0].isalpha():
            print(f"{list(obj.keys())[0]}: {list(obj.values())[0]}")
    print("============= END ===============")
main()