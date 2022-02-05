import sys
from unidecode import unidecode


def import_from_file(path_file):
    """Returns a word list from words in a file"""
    word_list = []
    with open(path_file, "r", encoding="utf-8") as f:
        for word in f:
            word_list.append(word.strip())
    print(f"Successfully imported {len(word_list)} words from {path_file}")
    return word_list


def starting_word():
    """Returns a starting word"""
    return "adieu"


def second_word():
    """Returns a second starting word"""
    return "rotis"


def help_cli():
    """Prints the command list"""
    print("'help' -> prints this help menu\n'exit' -> exit the program\n'play' -> start the game\n")


def play(wordlist, n = 5, max_tries = 7):
    """Start playing wordle"""
    print("For each try, enter your word then enter the result :  '-' if the letter isn't in the word, lowercase if it's the wrong place and upper if it's the correct letter.")
    print("For example: 'Adieu' then 'A--e-'")
    print(f"You can try '{starting_word()}' then '{second_word()}' to start with.\n")
    
    word = "-" * n
    letters = []
    wrong_letters = []
    advice = wordlist.copy()

    for tries in range(1, max_tries + 1):
        print(f"* Try {tries}:")
        advice = possible_words(advice, word, letters, wrong_letters, n)
        print(f"{len(advice)} words possibles")
        if len(advice) < 100:
            print(advice)
        word = guess(wordlist, word, letters, wrong_letters, n)
        print()


def guess(wordlist, word, letters, wrong_letters, n):
    """One try"""
    print(f"\tCurrent word: {word}\n\tWith: {letters}\n\tWithout: {wrong_letters}")
    user_input = unidecode(input("\tYour word:\n> ").strip().upper())
    print(f"\tYour word : {user_input}")
    result = unidecode(input("\tResult:\n> ").strip())
    print(f"\tYour result: {result}")
    word = update_word(word, letters, wrong_letters, user_input, result, n)
    return word


def possible_words(wordlist, found_word, letters, wrong_letters, n):
    advice = []
    for word in wordlist:
        w = word.upper()
        ispossible = True
        # Check right letters
        for l in letters:
            if l not in w:
                ispossible = False
        # Check wrong letters
        for l in wrong_letters:
            if l in w:
                ispossible = False
        # Check exact letters
        for i in range(n):
            if found_word[i] != '-' and found_word[i] not in w[i]:
                ispossible = False
        if ispossible: advice.append(word)
    return advice


def update_word(word, letters, wrong_letters, user_input, result, n):
    """Updates word, letters and wrong_letters based on the user_input and its results"""
    for i in range(n):
        l = result[i]
        if l == "-" and l.upper() not in wrong_letters:
            wrong_letters.append(user_input[i].upper())
        elif l.isupper():
            li = list(word)
            li[i] = l.upper()
            word = ''.join(li)
        elif l.islower() and l.upper() not in letters:
            letters.append(l.upper())
            letters.sort()
        else:
            print(f"Invalid input {user_input}", file=sys.stdout)
    return word


def cli(word_list):
    """Interactive CLI"""
    print("'help' for command list")
    running = True
    while running:
        action = input("> ")
        if action == "help":
            help_cli()
        elif action == "exit":
            running = False
        elif action == "play":
            play()
        else:
            print("See 'help' for the action list")


def main():
    try:
        word_list = import_from_file(sys.argv[1])
    except IndexError:
        print("Usage 'wordle.py word_list.txt'", file=sys.stderr)
        exit(1)
    # cli(word_list)
    play(word_list, 5, 7)


if __name__ == "__main__":
    main()
