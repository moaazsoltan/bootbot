import sys
from stats import get_num_words, get_num_charcters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(sys.argv[1])} total words")
print("--------- Character Count -------")

num_of_charcters = get_num_charcters(sys.argv[1])

for char in num_of_charcters:
    print(f"{char[0]}: {char[1]}")


print("============= END ===============")

