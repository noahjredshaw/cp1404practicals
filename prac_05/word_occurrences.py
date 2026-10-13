"""
Word Occurrences
Estimate: 25 minutes
Actual:   11! minutes
"""

word_to_count = {}
longest_word = 0
text = input("Text: ")
for word in text.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
    if len(word) > longest_word:
        longest_word = len(word)
for word, count in sorted(word_to_count.items()):
    print(f"{word:{longest_word}} : {count}")
