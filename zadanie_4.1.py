def polindrom(word_to_check):
    symbols_to_ignore = ("$", "!", " ", "?", ":" , ",", "&", "%")
    for i in word_to_check.lower():
        if i in symbols_to_ignore:
            word_to_check = word_to_check.replace(i, "")
        else:
            pass
    if word_to_check == word_to_check[::-1]:
        return True
    else:
        pass
        return False
