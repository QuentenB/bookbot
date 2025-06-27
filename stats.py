import string

def get_num_words(text):
    woordenLijst = text.split()
    teller = 0
    for i in range(0, len(woordenLijst), 1):
        teller += 1
    return teller

def get_num_letters(text):
    woorden_teller = {}
    for character in text:
        kleine_letter = character.lower()
        if kleine_letter in woorden_teller:
            woorden_teller[kleine_letter] += 1
        else:
            woorden_teller[kleine_letter] = 1
    return woorden_teller

