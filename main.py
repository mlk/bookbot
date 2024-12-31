path_to_file = "books/frankenstein.txt"

def numberOfWords(string):
    return string.split().__len__()

def characters(string):
    chars = {}
    for char in string.lower():
        if(char.isalpha()):
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def main():
    print(f"-- Begin report of {path_to_file} ---")

    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"{numberOfWords(file_contents)} words found in the document")
        map = characters(file_contents)
        for key, value in map.items():
            print(f"The '{key}' character was found {value} times")

if __name__ == "__main__": main()
