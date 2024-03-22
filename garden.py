# Loads the spaCy library for natural language processing tasks
import spacy 

# Load the English language model provided by spaCy
nlp = spacy.load ("en_core_web_sm")

# List is created with garden path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The horse race past the barn fell.",
    "Bengali banks sued by 3 foot aliens"
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize each sentence in the list, and perform named entity recognition.
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    
    print([(h, h.label_, h.label) for h in doc.ents])


# Explanations for named entity is displayed 
print(f"NORP: {spacy.explain('NORP')}")
print(f"QUANTITY: {spacy.explain('QUANTITY')}")
print(f"PERSON: {spacy.explain('PERSON')}")
print(f"GPE: {spacy.explain('GPE')}")

# Comment about two entities

# NORP:
# The NORP entity is for nationalities, religious or political groups
# The entity was used to categorise the word "Bengali" 
# This makes sense because "Bengali" is a nationality used to describe people from Bangladesh 

# GPE:
# The GPE entity is for countries, cities and states
# The entity was used to categorise the word "Mississippi"
# Mississippi is a state in USA