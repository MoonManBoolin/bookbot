def get_word_count(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

def get_char_count(book_text):
    char_dict = {}
    for char in book_text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_list(char_dict):
    char_list = []
    for char in char_dict:
        test = {}
        test[char] = char_dict[char]
        char_list.append(test)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(char_dict):
    return list(char_dict.values())[0]
        