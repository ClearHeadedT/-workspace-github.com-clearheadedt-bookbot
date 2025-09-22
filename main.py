import sys
from stats import *


def get_book_text(filepath):
    with open(filepath) as f:
        content_string = f.read()
    return content_string


def main():
    if len(sys.argv) < 2:
        return print("Usage: python3 main.py <path_to_book>"), sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        characters_in_book = character_counter(book)
        words_in_book = word_counter(book)
        frank_dict = sorted_dictionary(characters_in_book)
        return print(f"""
============ BOOKBOT ============\b
Analyzing book found at {sys.argv[1]}...\b
----------- Word Count ----------\b
Found {words_in_book} total words\b
--------- Character Count -------\b
{frank_dict}\b
============= END ===============
                """)
    
main()
