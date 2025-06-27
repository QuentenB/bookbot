def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def woorden_teller(text):
    woordenLijst = text.split()
    teller = 0
    for i in range(0, len(woordenLijst), 1):
        teller += 1
    return teller

def main():
    text = get_book_text("books/frankenstein.txt")
    woorden_teller(text)
    
main()
