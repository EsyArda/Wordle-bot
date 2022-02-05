from encodings import utf_8
import sys
import unidecode


def file_to_word_list(file_path):
    """Returns a list with the first word of each line in a file"""
    word_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        f.readline()  # pass first title line
        for line in f:
            # remove accents
            l = unidecode.unidecode(line).strip().split("\t")
            word_list.append(l[0])  # first word of each line
        f.close()
    return word_list


def filter_word_by_length(word_list, n):
    """Returns a new list with each string of n characters"""
    l = []
    for word in word_list:
        if len(word) == n:
            l.append(word)
    return l


def list_to_file(word_list, file_path):
    """Prints all word from the list in a file"""
    with open(file_path, "w", encoding="utf_8") as f:
        for word in word_list:
            f.write(word + "\n")


def main():
    word_list = file_to_word_list("Lexique/Lexique383.tsv")
    five_letters = filter_word_by_length(word_list, 5)
    list_to_file(five_letters, "./wordle_list.txt")


if __name__ == "__main__":
    main()
