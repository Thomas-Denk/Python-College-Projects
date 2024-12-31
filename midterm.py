import nltk
from textblob import TextBlob
# For these methods, I am using an excerpt from the story Snow White to demonstrate
x = 0

b = TextBlob("The Queen couldn’t bear it. She was so jealous and ngry that she ordered a huntsman to take Snow White into the woods and kil her. She told him to return with her heart as proof of her death.")
List1 = ["Snow White", "And", "The", "Seven Dwarfs"]
print("Our text excerpt is taken from the first section of the story...")
print(List1)
print()

print("Method 1: work_counts can return the number of times a word occurs in the text blob. This could be useful for word analysis in fields such as marketing or data analytics. Incorrect spelling in text is intentional as it will be useful for testing Method 2. See example below.")

print()


print(b.word_counts)

while x == 0:
    print()
    print("Method 2: correct() will attempt to correct any misspellings in the text. In our case, angry and kill are misspelled and this method corrects this in the return. See example below.")
    print()
    print(b.correct())
    print()
    x = x + 1

if x == 1:

    print("Method 3: title() returns the entire text in titlecase format. See example below.")
    print()
    print(b.title())
    x = x + 1





