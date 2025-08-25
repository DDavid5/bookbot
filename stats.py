def get_book_text (path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_book):
    file_content = get_book_text(path_to_book)
    count=0
    words = file_content.split()
    for word in words:
        count += 1
    return count

def letter_counter(path_to_book):
    file_content = get_book_text(path_to_book).lower()
    letters = {}
    for letter in file_content:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    sorted_letters = dict(sorted(letters.items(),key=lambda item: item[1],reverse=True))
    return sorted_letters

def report(path_to_book):
    count = get_num_words(path_to_book)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")
    print(f"============= END ===============")
    sorted=letter_counter(path_to_book)
    for k, v in sorted.items():
        print(f"{k}: {v}")