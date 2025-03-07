from bloomfilter import BloomFilter
import math
import sys

# usage: python spellcheck.py <filename> <words to spell check>
# example command: python spellcheck.py "/Users/umaparhar/Learning:Projects/BloomFilterSpellChecker/test" A Ab ABBBBBB
arguments = sys.argv

if len(arguments) <= 1:
    print("No arguments provided")

# assumes you have already created your bloom filter & saved it to a file
# if no bf has been created/saved, use the insert functions to insert your items into the BF
filename = arguments[1]

def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

def generate_params(filename):
    dict_size = count_lines(filename)

    desired_false_positive = 0.01

    bf_size = int(-(dict_size*math.log(desired_false_positive))/(math.log(2)) ** 2)

    hash_number = int(bf_size/dict_size * math.log(2))
    return [bf_size, hash_number]

bf = BloomFilter()
bf.load_from_file(filename)

incorrect_words = []

for a in arguments[2:]:
    found = bf.query_bloom(a)
    if not found:
        incorrect_words.append(a)

print(f"Incorrectly spelled words:")

for word in incorrect_words:
    print(word)


