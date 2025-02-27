def get_books_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(words):
    num_words = len(words.split())
    return num_words 

def count_characters(words):
    letters = {}  
    for char in words:   
        char = char.lower()
        if char.isalpha():  
            if char in letters:  
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def sorted_list_of_dicts(letters):
    lists = list(letters.items())
    lists.sort(key=lambda item: item[1], reverse=True)
    sorted_list = [{char: count} for char, count in lists]
    return sorted_list
    

