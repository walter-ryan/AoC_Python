# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

with open('./2015/05/input.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def three_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    if count >= 3:
        return True
    return False

def double_letters(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def contains_string(word):
    for i in range(len(word)-1):
        if word[i]+word[i+1] in ["ab", "cd", "pq", "xy"]:
            return True
    return False

goodCount = 0

for word in lines:
    if three_vowels(word) and double_letters(word) and not contains_string(word):
        goodCount += 1

print("The count of good words is:", goodCount)