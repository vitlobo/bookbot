from stats import get_num_words, get_times_used, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #character_count = get_times_used(text.lower())
    c_count_list = sort_dict(get_times_used(text.lower()))

    print(f'''============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
found {num_words} total words
--------- Character Count -------''')

    for l in c_count_list:
        this_char  = l["char"]
        this_value = l["num"]
        if this_char.isalpha() == True:
            print(f"{this_char}: {this_value}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()