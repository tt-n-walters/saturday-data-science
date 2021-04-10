import requests
from bs4 import BeautifulSoup
import nltk           # pip install nltk
import matplotlib.pyplot as plt


url = "https://en.wikipedia.org/wiki/Fictional_universe_of_Harry_Potter"
response = requests.get(url)

soup = BeautifulSoup(response.text, features="html.parser")
page_text = soup.find(id="mw-content-text")

complete_text = page_text.text               # corpus
print("Total length:", len(complete_text))

lines = complete_text.splitlines()
print("Number of lines:", len(lines))

words = complete_text.split()
print("Estimated number of words:", len(words))
print("Estimated average length of word:", len(complete_text) / len(words))

tokens = nltk.word_tokenize(complete_text)

filtered_tokens = []
for token in tokens:
    if token.isalpha():
        filtered_tokens.append(token.lower())

print("Filtered words:", len(filtered_tokens))
print(filtered_tokens.count("and"))

word_counts = {}
def count_words(word):
    count = filtered_tokens.count(word)
    word_counts[word] = count


for fil in filtered_tokens:
    count_words(fil)

a, b = 10, 20

print("'and' appears:", word_counts["and"])
print(len(word_counts))
print(word_counts)

most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print(most_common[:20])

words = []
counts = []
for word, count in most_common[:20]:
    words.append(word)
    counts.append(count)

plt.bar(words, counts)
plt.show()