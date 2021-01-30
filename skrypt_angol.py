def read_file(txt_name):
    with open(str(txt_name)+".txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines

def swap_txt(lines):
    swapped_line = []
    for i in range(0, len(lines)):
        actual_line = lines[i]
        if actual_line.find(" - ") != -1:
            english_word = str(actual_line[:actual_line.find(" - ")]).strip()
            polish_word = str(actual_line[actual_line.find(" - ")+3:]).strip()

        elif actual_line.find(" = ") != -1:
            english_word = str(actual_line[:actual_line.find(" = ")]).strip()
            polish_word = str(actual_line[actual_line.find(" = ")+3:]).strip()
        swapped_line.append([polish_word,english_word])

    polish_words_list = [x for x,y in swapped_line]
    polish_words_list.sort(key = sort_key)
    to_print = [[x,y] for x in polish_words_list for a,y in swapped_line if a==x]

    with open("output.txt", "w") as f:
        for word in to_print:
            f.write(word[0] + " - " + word[1] + "\n")


def sort_key(n):
    #sort method key for words containing polish letters
    tab = []
    for _ in n:
        polish_alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
        d = {i:polish_alphabet.index(i) for i in polish_alphabet}
        if _ in d.keys():
            tab.append(d[_])
        else:
            pass
    return tab




def main():
    file = input("NAZWA PLIKU (.txt): ")
    swap_txt(read_file(file))


if __name__ == "__main__":
    main()
