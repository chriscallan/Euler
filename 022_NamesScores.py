# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
import json

ASCII_OFFSET = 64       # used to get the alphabetical index of each letter (assumes all-caps)

def name_summer(in_name):
    retval = 0
    for letter in in_name:
        retval += (ord(letter) - ASCII_OFFSET)
    return retval

names_list = []
with open("./data_files/p022_names.txt", 'r') as namesfile:
    for line in namesfile:
        names = (x.replace('"', '') for x in line.split(","))
        names = sorted(names)
        for name in names:
            pos_idx = list(names).index(name) + 1
            name_summed = name_summer(name)
            ranking = pos_idx * name_summed
            names_list.append(json.dumps({"name": name, "position": pos_idx, "value": name_summed, "ranking": ranking}))
            # names_list.append('{{ "name": {0}, "position": {1}, "value": {2}, "ranking": {3} }}'.
            #                   format(name, pos_idx, name_summed, ranking))
print("names_list is: {0}".format(names_list))
all_name_scores = 0
for scores in names_list:
    temp_json = json.loads(scores)
    print("temp_json is: {0}".format(temp_json))
    all_name_scores += temp_json["ranking"]
print("total of all rankings is: {0}".format(all_name_scores))