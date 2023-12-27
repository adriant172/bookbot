def main():
    book = "books/frankenstein.txt"
    with open(book, encoding="UTF-8") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
        print(f"--- Beginning report of {book} ---")
        print(f"{word_count} words were found in the document")
        print(" ")
        new_letter_list = convert_to_list(letter_count)
        for letter in new_letter_list:
            if letter[0].isalpha():
                print(f"The \'{letter[0]}\' character was found {letter[1]} times")
        print("--- End Report ---")
        


def count_words(book_text):
    words = book_text.split()
    num_of_words = len(words)
    return num_of_words

def count_letters(book_text):
    words = book_text.split()
    letter_count = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def convert_to_list(letter_dict):
    list_of_letters = []
    for letter in letter_dict:
        list_of_letters.append((letter ,letter_dict[letter]))
    list_of_letters.sort()
    return list_of_letters


main()
