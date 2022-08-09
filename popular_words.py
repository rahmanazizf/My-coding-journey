import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#prompt file name that is about to be opened from user
fname = input("Enter the file name: ")
#handling file, opening and reading it, then split the words by whitespace
fhand = open(fname).read().split()
#creating empty dict to store words as keys and its number as the values
words = {}
#looping in fhand
for word in fhand:
    if len(word) > 4:
        word = word.upper() #making it upper so that there will be no differences between the same word upper or lower
        words[word] = words.get(word, 0) + 1 #storing word, if word is already in words then it returns value
    #but if not, it sets assigned value to the new word
#print(words)

#most popular word
most_pop_word = str
most_count = 0
for word, count in words.items():
    if most_count < count and len(word) > 4:
        most_pop_word = word
        most_count = count
#print(most_pop_word, most_count)
W = [word for word in words.keys()]
C = [count for count in words.values()]
pop_w = pd.DataFrame({'Word':W, 'Count':C})
pop_w = pop_w.sort_values(by='Count', ascending=False).iloc[:5, :2]
print(pop_w)
sns.barplot(data=pop_w, x='Word', y='Count')
plt.title("Top 5 Most Used Words in {article}".format(article = fname))
plt.show()

