def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def count_char(book_text):
    char_count = {}

    for char in book_text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    
    return char_count

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_info = {"char" : char, "num" : count}
        char_list.append(char_info)
    
    char_list.sort(key = lambda x: x["num"], reverse=True)

    return char_list

