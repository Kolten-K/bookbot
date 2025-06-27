import sys

from stats import get_num_words
from stats import get_num_character
from stats import create_character_amount_list
from stats import num_character_sort

def get_book_text(path):
        with open(path) as f:
                file_contents = f.read()
        return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = get_book_text(sys.argv[1])
	num_words = get_num_words(sys.argv[1])
	num_character = get_num_character(sys.argv[1])
	sorted_list = create_character_amount_list(num_character)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at ...{sys.argv[1]}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for i in sorted_list:
		character =i["char"]
		count =i["num"]
		if character.isalpha():
			print(f"{character}: {count}")
	print("============= END ===============")
main()
