# Deixar mais profissa
# Usar argparser
# Remodelar para usar POO
# Webfront talvez???

def wordToAsterisk(word):
    return len(word) * '*'

def sWiTcHcAsE(word):
    finalWord = ""
    for w, char in enumerate(word):
        if w % 2 == 0:
            finalWord += char.upper()
        else:
            finalWord += char.lower()

    return finalWord

def main():
    # funcoes pra chamar
    while True:
        option = int(input("Enter your choice: 1. Word to '*'\n2. sWiTcH cAsE"))
        if option == 1:
            word = input(str("Enter your word: "))
            print(wordToAsterisk(word))

        if option == 2:
            wordSwitchCase = input(str("EnTeR yOuR wOrD: "))
            print(sWiTcHcAsE(wordSwitchCase))

        if option == 3:
            break


if __name__ == "__main__":
    main()