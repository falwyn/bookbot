import sys

from stats import count_words
from stats import count_chars
from stats import get_dict_list



def main():
    # print(get_book_text("books/frankenstein.txt"))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    file_path = sys.argv[1]



    char_dict = count_chars(file_path)

    dict_list = get_dict_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_path)} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()
