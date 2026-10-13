"""
Word Occurrences
Estimate: 25 minutes
Actual:   ... minutes
"""

text_to_count = {}
# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
for word in text.split():
    if word in text_to_count:
        text_to_count[word] += 1
    else:
        text_to_count[word] = 1
for word, count in sorted(text_to_count.items()):
    print(f"{word} : {count}")
