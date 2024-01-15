def get_text(path : str):
    with open(path) as f:
        return f.read()

def count_text(text: str) -> int: 
    count = len(text.split())
    return count


def count_letters(text: str):
    count = {}
    for i in text:
        if(i.isalpha()):
            letter = i.lower()
            count[letter] = count.get(letter,0)+1
    return count

def sorted_list(dict):
    letter_count_list = []
    for letter, count in dict.items():
        letter_count_list.append((count,letter))
    letter_count_list = sorted(letter_count_list)
    return letter_count_list

def main():
    path = "./books/frankenstein.txt"
    file_contents = get_text(path)
    words_count = count_text(file_contents)
    letter_count_dict = count_letters(file_contents)
    letter_count_list = sorted_list(letter_count_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document")
    print()
    for x,y in letter_count_list:
        print(f"The '{y}' character was found {x} times")
    print("--- End of report ---")

main()
