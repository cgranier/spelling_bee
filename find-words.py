# Find solutions to the NYT's Spelling Bee puzzle.
# letters = the 7 letters in the day's puzzle
# required_letter = the middle letter of the puzzle
# Output: a list of potential solution words in order from
# longest to shortest and then in alphabetical order.
# Uses the official Scrabble dictionary, Collins 2019 edition.
# Not all solutions will be valid in the NYT puzzle.

def find_words(letters, required_letter):
    words = []
    with open("collins.txt", "r") as wordfile:
        for word in wordfile:
            word = word.strip()
            if len(word) > 3:
                if set(word).issubset(letters) and required_letter in word:
                    words.append(word)
    return words

letters = set("HNEPATHY")
required_letter = 'Y'

solution = find_words(letters, required_letter)
# Sort the list by length (from longer to shorter) and the alphabetically for each length
sorted_solution = sorted(sorted(solution, key=lambda i: i), key=lambda i: -len(i))

for word in sorted_solution:
    print(word)
