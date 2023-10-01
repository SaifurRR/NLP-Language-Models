import spacy #named entity recognition, part-of-speech tagging, dependency parsing
from nltk import Tree #represent syntactic structures and parse trees
from squids import squids_text #custom text from .py script

dependency_parser = spacy.load('en')# loads spaCy language model for English

parsed_squids = dependency_parser(squids_text)#extract grammatical relationship between words in a text

# Assign my_sentence a new value:
my_sentence = "It's so cold in here!"
my_parsed_sentence = dependency_parser(my_sentence)

def to_nltk_tree(node): #node: tokens in a sentence
  if node.n_lefts + node.n_rights > 0:
    #any word (l/r) dependent on node
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    #recursively calls the func, list of children of a node
    return Tree(node.orth_, parsed_child_nodes)
    #creates Tree using NLTK Class, includes parent & children;
    #node.orth_: label for current node(parent node) 
  else:
    return node.orth_ #parent node

for sent in parsed_squids.sents:
  to_nltk_tree(sent.root).pretty_print() #sent.root : main verb of the sentence
#access individual sentences and parse each of them into 'tree' structure.

for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()