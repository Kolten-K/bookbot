def get_num_words(path):
        with open(path) as f:
                file_contents = f.read()
                words = file_contents.split()
                num_words = len(words)
        return num_words
def get_num_character(path):
	with open(path) as f:
		file_contents = f.read()
		characters = file_contents.lower()
		character_amount = {}
		for i in characters:
			if i in character_amount:
				character_amount[i] += 1
			else:
				character_amount[i] = 1
		return character_amount
def create_character_amount_list(character_amount):
	character_amount_list = []
	for key, value in character_amount.items():
		temp = {"char" : key, "num" : value}
		character_amount_list.append(temp)
	character_amount_list.sort(reverse=True, key=num_character_sort)
	return character_amount_list
def num_character_sort(items):
	return items["num"]
