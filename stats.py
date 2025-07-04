def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def count_words(file_path):
    content = get_book_text(file_path)
    content_splitted = content.split()

    return len(content_splitted)


def count_chars(file_path):
    content = get_book_text(file_path)
    content = content.lower()

    char_dict = {}

    for char in content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def get_dict_list(char_dict):
    dict_list = []

    for key, value in char_dict.items():
        small_dict = {"char": f"{key}", "num": value}
        dict_list.append(small_dict)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
