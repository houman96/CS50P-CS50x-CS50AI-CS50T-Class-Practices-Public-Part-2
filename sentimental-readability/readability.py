from cs50 import get_string

text = get_string("Text: ")

count = 0
letter_count = 0
word_count = 0
sentence_count = 0

for c in text:
    if c == " ":
        word_count += 1
    elif c == "!" or c == "." or c == "?":
        sentence_count += 1
    elif c.isalpha():
        letter_count += 1

word_count += 1

l = 100 * letter_count / word_count
s = 100 * sentence_count / word_count
result = (0.0588 * l) - (0.296 * s) - 15.8
index = round(result)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(("Grade {}").format(index))
