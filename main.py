from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    aantalWoorden = get_num_words(text)
    print(f"{aantalWoorden} words found in the document")

main()
