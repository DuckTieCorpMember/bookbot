import sys
from stats import get_word_count, get_char_count, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}')
    print("----------- Word Count ----------")
    print(f'Found {get_word_count(text)} total words')
    print("--------- Character Count -------")
    char_dict = get_char_count(text)
    sorted_dict = sort_dict(char_dict)
    for key,value in sorted_dict.items():
        if key.isalpha():
            print(f'{key}: {value}')
    print("============= END ===============")

main()        