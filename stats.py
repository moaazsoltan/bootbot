def get_num_words(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
        number_of_words = len(file_contents.split())
        return number_of_words

def get_num_charcters(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read().lower()
        letter_count: dict[str, int] = {}
        for letter in file_content:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) +1

    sorted_by_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

    return sorted_by_count
        