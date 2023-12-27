def main():
    with open("books/frankenstein.txt", encoding="UTF-8") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"Word count: {word_count}")


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
                letter_count[letter] = 0
    print(letter_count)

main()
