from difflib import get_close_matches, SequenceMatcher
import re


def get_words(option):
    if option == 1:
        TEXT = open("mywords.txt").read()
        return re.findall("[a-z]+", TEXT.lower())
    elif option == 2:
        TEXT = open("nepali_words.txt").read()
        return TEXT.split()


def check_word(word):
    most_probable = None
    if word not in WORDS:
        suggestion = get_close_matches(word, WORDS)

        if len(suggestion) < 1:
            most_probable = "No matching words!"
        else:
            most_probable = "Did you mean {suggestion} ?".format(
                suggestion=suggestion[0]
            )

        seq = SequenceMatcher(a=word, b=suggestion[0])

        print(most_probable)

        print("Probability of match is: {prob}".format(prob=seq.ratio()))
    else:
        print("Spelling is correct!")


languageOption = input("Enter 1 for English or 2 for Nepali:")
WORDS = get_words(int(languageOption))

s = input("Enter string:").lower()
check_word(s)