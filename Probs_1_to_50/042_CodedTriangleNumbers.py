# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
#   we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
#   triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
#   English words, how many are triangle words?


# first generate the list of 'triangle numbers'
tri_list = {}
for i in range(1, 100):
    temp = i * (i + 1) // 2
    tri_list[str(i)] = temp

ascii_offset = 64   # 'A' is 65, and we need that to be '1' since it's the first letter of the alphabet
final_answer = []
with open("./data_files/p042_words.txt") as their_words:    # slurp up the file now
    for line in their_words.readlines():
        word_list = line.split(",")
        for word in word_list:
            word_work = word.replace("\"", "")  # don't need the quotes around each word
            temp_val = 0
            for letter in word_work:        # time to tally the totals
                temp_val += ord(letter) - ascii_offset
            if temp_val in tri_list.values():   # keep track of the tallies that were in our dictionary
                final_answer.append(word)

print("final answer is: {0}".format(len(final_answer)))
