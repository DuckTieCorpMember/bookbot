def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}

    for char in list(text.lower()):
        if char in char_dict:
            char_dict[char] =  1 + char_dict[char]
        else:
            char_dict[char] =  1

    return char_dict

def sort_dict(dict_items: dict):
    sorted_dict = dict(sorted(dict_items.items(), key=lambda x:x[1], reverse=True))
    return sorted_dict