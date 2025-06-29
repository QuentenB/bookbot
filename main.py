from stats import get_num_words, get_num_letters, sorted_dic, sorteer_op

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")

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
