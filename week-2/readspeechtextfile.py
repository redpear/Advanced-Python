# START

# Import the regular expression module
import re

# Import Counter
from collections import Counter

# Open the Obama 2016 State of the Union text file
# file = open("Obama_2016_State_of_the_Union.txt", "r")
file = open("/Users/angieburk/Documents/Advanced Python/week-2/Obama_2016_State_of_the_Union.txt", "r")
# Read the speech from the file
speech = file.read()

# Close the file
file.close()

# Find all of the words in the speech
words = re.findall(r'\b\w+\b', speech)

# Count the total number of words
word_count = len(words)

# Count the total number of characters
character_count = len(speech)

# Set the total word length to 0
total_word_length = 0

# FOR each word in the speech
   # Add the length of the word to the total word length
# END FOR
for word in words:
    total_word_length = total_word_length + len(word)

# Calculate the average word length by dividing the total word length by the number of words
average_word_length = total_word_length / word_count

# Split the speech into sentences using periods, exclamation points, and question marks
sentences = re.split(r'[.!?]', speech)

# Set the sentence count to 0
sentence_count = 0


# FOR each sentence
    # IF the sentence is not empty
        # Add 1 to the sentence count
    # END IF
# END FOR

for sentence in sentences:
    if sentence.strip() != "":
        sentence_count = sentence_count + 1

# Calculate the average sentence length by dividing the word count by the sentence count
average_sentence_length = word_count / sentence_count

# Create an empty list for lowercase words
lowercase_words = []

# FOR each word
   #  Convert the word to lowercase
    # Add the lowercase word to the list
# END FOR

for word in words:
    lowercase_words.append(word.lower())

# Count how many times each word appears
word_frequency = Counter(lowercase_words)

# Find the ten longest words
unique_words = set(lowercase_words)
sorted_words = sorted(unique_words, key=len, reverse=True)
longest_words = sorted_words[:10]

# Display the results
# Display the results
print("STATE OF THE UNION SPEECH ANALYSIS")
print("------------------------------------------")

print("Statistic\t\t\tResult")
print("------------------------------------------")
print("Word Count\t\t\t", word_count)
print("Character Count\t\t\t", character_count)
print("Average Word Length\t\t", round(average_word_length, 2))
print("Average Sentence Length\t\t", round(average_sentence_length, 2))
print

# Display the word frequency
print("\nWORD FREQUENCY")
print("------------------------------------------")
print("Word\t\t\tFrequency")
print("------------------------------------------")

for word, count in word_frequency.items():
    print(word, "\t\t\t", count)


# Display the ten longest words
print("\nTOP TEN LONGEST WORDS")
print("------------------------------------------")
print("Word\t\t\tLength")
print("------------------------------------------")

for word in longest_words:
    print(word, "\t\t\t", len(word))

# END