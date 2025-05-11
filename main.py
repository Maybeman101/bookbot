import sys
from stats import get_num_words, count_char, sort_chars


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    with open(file_path) as f:
        book_text = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text}...")
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)

    print(f"Found {word_count} total words")
   
    characters = count_char(book_text)
    char_count = sort_chars(characters)
    print("--------- Character Count -------")
    for char_info in char_count:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")


main()