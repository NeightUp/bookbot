def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    generate_report(text, book_path)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        c = char.lower()
        if c.isalpha():
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
    sorted = sort_letters(letters)
    return sorted

def sort_on(dict):
    return dict["value"]

def sort_letters(letters_dict):
    letter_dicts = []
    for key in letters_dict:
        l_dict = {"letter" : key, "value" : letters_dict[key]}
        letter_dicts.append(l_dict)
    letter_dicts.sort(reverse=True, key=sort_on)
    return letter_dicts

def generate_report(text, path):
    word_count = count_words(text)
    letters_list = count_letters(text)

    print()
    print(f"--- Analysis of {path} ---")
    print(f"{word_count} words found in {path}")
    print()
    
    for item in letters_list:
        print(f"The '{item["letter"]}' character was found {item["value"]} times")
    print()
    print("--- End Report ---")

main()