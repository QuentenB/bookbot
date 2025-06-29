from stats import get_num_words, get_num_letters, sorted_dic, sorteer_op
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    aantalWoorden = get_num_words(text)
    aantalLetters = get_num_letters(text)

    print(f"Found {aantalWoorden} total words")

    #for letter, aantal in sorted(aantalLetters.items()):
        #print(f"'{letter}': {aantal}")
    
    sorted_list = sorted_dic(aantalLetters)
    sorted_list.sort(key=sorteer_op, reverse=True)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    
    
    
main()
