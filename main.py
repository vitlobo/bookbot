import sys
from stats import (
    get_num_words,
    get_times_used,
    sort_dict,
)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_times_used(text.lower())
    c_sorted_list = sort_dict(get_times_used(text.lower()))
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