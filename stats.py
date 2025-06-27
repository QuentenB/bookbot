def get_num_words(text):
    woordenLijst = text.split()
    teller = 0
    for i in range(0, len(woordenLijst), 1):
        teller += 1
    return teller