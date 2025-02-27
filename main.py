import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1] 

from stats import count_words, count_characters, sorted_list_of_dicts



def main ():
    words = get_books_text(path_to_file)
    number_of_words = count_words(words)
    letters = count_characters(words)
    sorted_dict = sorted_list_of_dicts(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_dict:
        for char, count in char_dict.items():
            print(f"{char}: {count:>5}")
    print("============= END ===============")


def get_books_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()