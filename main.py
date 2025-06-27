from stats import get_num_words, get_num_letters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    aantalWoorden = get_num_words(text)
    aantalLetters = get_num_letters(text)
    print(f"{aantalWoorden} words found in the document")
    for letter, aantal in sorted(aantalLetters.items()):
        print(f"'{letter}': {aantal}")
    
main()
