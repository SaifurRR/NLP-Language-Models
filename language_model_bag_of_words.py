# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords #words: little to no significance
from nltk.tokenize import word_tokenize #separate each words
from nltk.stem import WordNetLemmatizer #reduce to base-word
# importing Counter to get word counts for bag of words
from collections import Counter
# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# Change text to another string:
text = "As humans, we can easily resolve ambiguity by examining the text for hints about elements like place and time that express the details of the conversation (such as understanding what happened between John and Luca, or whether the conversation is about a computer when mentioning the mouse)."

cleaned = re.sub('\W+', ' ', text).lower() #remove symbol punctuation
tokenized = word_tokenize(cleaned)  #list of words

stop_words = stopwords.words('english') #retrieves English stopwords
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer() #lemmatize words
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered] # apply lemmatizer to each token
# Comment out the print statement below
#print(normalized)

# Define bag_of_looking_glass_words & print:
bag_of_looking_glass_words=Counter(normalized)
print(bag_of_looking_glass_words)



