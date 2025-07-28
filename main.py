import sys
from stats import (
    get_num_words,
    get_times_used,
    sort_dict,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_times_used(text.lower())
    c_sorted_list = sort_dict(character_count)
    print_report(book_path, num_words, c_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, c_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for l in c_sorted_list:
        if l["char"].isalpha() == True:
            print(f"{l["char"]}: {l["num"]}")

    print("============= END ===============")

main()