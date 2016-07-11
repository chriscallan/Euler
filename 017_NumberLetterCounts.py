# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.


digits_english = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                  9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                  30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
k = 1000
running_total = ""

for i in range(1, 1001):
    if i <= 20:
        running_total += digits_english.get(i)
    elif 20 < i < 100:
        ones = digits_english.get(i % 10)
        running_total += "{0}{1}".format(digits_english.get(int(i / 10) * 10),
                                            ("" if str(ones).__eq__("zero") else "-{0}".format(ones)))
    elif 100 <= i < 1000:
        hundreds = digits_english.get(int(i / 100))
        if i - int(i / 100) * 100 > 20:
            tens = digits_english.get(int((i - (int(i / 100) * 100)) / 10) * 10) + "-"
            ones = digits_english.get((i - (int(i / 100) * 100)) % 10)
        else:
            tens = digits_english.get(i - (int(i / 100) * 100))
            ones = "zero"
        try:
            temp_string = "{0} hundred{1}{2}{3} ".format(hundreds, ("" if str(tens).__eq__("zero")
                                                                        and str(ones).__eq__("zero") else " and "),
                                                           "" if str(tens).__eq__("zero") else tens,
                                                           "" if str(ones).__eq__("zero") else ones)
            temp_string = temp_string.strip(" ")
            running_total += temp_string
        except Exception as exc:
            print("current vals are: {0}".format(running_total))
    else:
        running_total += "one thousand"
    running_total += "" if i == 1000 else ", "
    # print("running total is: {0}".format(running_total))
print("running_total is: {0}".format(running_total))
mod_total = running_total.replace(" ", "").replace("-", "").replace(",", "")
print("length is: {0}".format(len(mod_total)))