import enchant

pwl = enchant.request_pwl_dict("mywords.txt")


def checkword():
    word = input("Enter a word:")
    suggest = pwl.suggest(word)
    try:
        print("Did you mean:" + suggest[0])
    except:
        print("No suggestion to word")


checkword()
