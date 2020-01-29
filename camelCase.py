# Write a program that turns a sentence into camel case. The first word is lowercase,
# the rest of the words have their initial letter capitalized, and all of the words are joined together.


def caseUp(sentence):
    # convert the first character in each word to Uppercase
    firstLetUp = sentence.title()

    # putting space between words
    camelCaseUp = firstLetUp.replace(' ', '')

    # return sentence with space between word
    # and first sentence word in lower case then other in capital
    return camelCaseUp[0:1].lower() + camelCaseUp[1:]


def main():
    # user input
    sentence = input('Enter your sentence: ')

    # calling method camelCase
    camelCased = caseUp(sentence)
    # Output
    print(camelCased)


if __name__ == '__main__':
    main()
