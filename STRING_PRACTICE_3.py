

def latest_letter(word):
    word.sort()
    return word[-1]
print(latest_letter(list('pterodactyl')))