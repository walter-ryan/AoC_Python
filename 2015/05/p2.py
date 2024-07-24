# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?


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

def matching_pairs(word):
    for i in range(len(word)-3):
        if word[i]+word[i+1] in word[i+2:]:
            return True
    return False

def sandwich_letters(word):
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False

goodCount = 0
print(matching_pairs("aaaa"))
for word in lines:
    if sandwich_letters(word) and matching_pairs(word):
        goodCount += 1

print("The count of good words is:", goodCount)