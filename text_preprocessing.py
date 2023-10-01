# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

cleaned = re.sub('\W+', ' ', text) 
# regex: substitute all non-word characters (symbols, punctuation, etc.) with a space
tokenized = word_tokenize(cleaned)
# break words, punctuation -> tokens/entity

stemmer = PorterStemmer() #algorithm to stem words
stemmed = [stemmer.stem(token) for token in tokenized] # remove prefix/suffix

## -- CHANGE these -- ##
lemmatizer = WordNetLemmatizer()
#reduce word to its base/canonical form
lemmatized = [lemmatizer.lemmatize(token,get_part_of_speech(token)) for token in tokenized]
#tell lemmatizer  -> 'part of speech' the word belongs to, by default lemmatize treats every word as noun

print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)