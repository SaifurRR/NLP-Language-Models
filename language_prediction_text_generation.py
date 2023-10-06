import nltk, re, random
from nltk.tokenize import word_tokenize
from collections import defaultdict, deque

training_doc1 = """

In the moonlit whispers of neon dreams,
Where stars embrace the city seams,
We dance in rhythms of midnight hues,
Under the canopy of midnight blues.

"""

training_doc2 = """
Electric heartbeat, a symphony of the night,
Painting constellations in celestial light,
Invisible strings pulling us high,
Chasing stardust trails across the sky.
"""

training_doc3 = """
Shadows waltz in a clandestine trance,
Silent melodies, a ghostly dance,
We're lost in echoes of forgotten lore,
In the moonlit abyss, we seek no more.
"""
class MarkovChain:
  def __init__(self):
    self.lookup_dict = defaultdict(list) # initializes a lookup dictionary to store word pairs and their possible next words; will store list of possible next words as values.
    self._seeded = False #untick seed (flag): which provides same seq. for a particular seed value
    self.__seed_me() #method responsible for seeding the generator based on the _seeded flag and the input seed

  def __seed_me(self, rand_seed=None): # Check if the generator is already seeded
    if self._seeded is not True:  
      try:
          if rand_seed is not None:  # If a specific seed is provided
            random.seed(rand_seed)  # Seed the generator with the specified seed
          else:
            random.seed()  # otherwise: seed the generator with a random seed
          self._seeded = True  # Update the _seeded flag to indicate successful seeding
      except NotImplementedError:
        self._seeded = False  # If seeding is not possible, update the _seeded flag accordingly      

  def add_document(self, str): #preprocesses the input text, generates word pairs,
  #and populates the lookup_dict by associating each word with the words that frequently follow it based on the input text.
    preprocessed_list = self._preprocess(str)  # Preprocess the input text 
    pairs = self.__generate_tuple_keys(preprocessed_list) #method to generate word pairs (e.g., [word1, word2], [word2, word3], ...)
  
    for pair in pairs:  #Iterates over the generated word pairs
        self.lookup_dict[pair[0]].append(pair[1])  # dictionary that contains list of words that comes often together
        #pair[0]: represents the current word, pair[1] represents the word that follows
        #lookup_dict : dictionary where the keys are words, and the values are lists of words 
  
  def _preprocess(self, str): #cleaning (replace alpha-numeric with spaces)
  # and tokenization: making it ready to use in 'Markov-chain'
    cleaned = re.sub(r'\W+', ' ', str).lower() #\W+: matches one/more sonseq. alphanumeric character, \W:matches one alphanumeric ch
    tokenized = word_tokenize(cleaned)
    return tokenized

  def __generate_tuple_keys(self, data): #preprocessed text is passed here to generate word pairs -> e.g., [word1, word2], [word2, word3]
  #generating pairs of adjacent words from the preprocessed text
    if len(data) < 1:
      return

    for i in range(len(data) - 1):
      yield [ data[i], data[i + 1] ]
      
  def generate_text(self, max_length=50):
    context = deque()
    output = []
    if len(self.lookup_dict) > 0:
      self.__seed_me(rand_seed=len(self.lookup_dict))
      chain_head = [list(self.lookup_dict)[0]]
      context.extend(chain_head)
      
      while len(output) < (max_length - 1):
        next_choices = self.lookup_dict[context[-1]]
        if len(next_choices) > 0:
          next_word = random.choice(next_choices)
          context.append(next_word)
          output.append(context.popleft())
        else:
          break
      output.extend(list(context))
    return " ".join(output)

my_markov = MarkovChain()
my_markov.add_document(training_doc1)
my_markov.add_document(training_doc2)
my_markov.add_document(training_doc3)
generated_text = my_markov.generate_text()
print(generated_text)