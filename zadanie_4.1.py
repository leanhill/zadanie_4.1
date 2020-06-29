
def polindrom(word_to_check):
    for i in range(int(len(word_to_check))):
        if word_to_check[i] == word_to_check[len(word_to_check) - i - 1]:
            c = bool(word_to_check)
        else:
            c = bool()
            break
    return(c)


