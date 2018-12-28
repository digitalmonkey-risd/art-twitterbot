import markovify
import nltk
import re
import itertools


text_a = open("ghost.txt").read()
text_b = open("carol.txt").read()

class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)

# change to "word" for a word-level model
level = "word"
# controls the length of the n-gram
order = 5
# controls the number of lines to output
output_n = 1
# weights between the models; text A first, text B second.
# if you want to completely exclude one model, set its corresponding value to 0
weights = [0.5, 0.5]
# limit sentence output to this number of characters
length_limit = 600


for _ in itertools.repeat(None, 1):
	model_cls = markovify.Text if level == "word" else SentencesByChar
	gen_a = model_cls(text_a, state_size=order)
	gen_b = model_cls(text_b, state_size=order)
	gen_combo = markovify.combine([gen_a, gen_b], weights)
	counter=0
	for i in range(output_n):
	    out = gen_combo.make_short_sentence(length_limit, test_output=False)
	    out = out.replace("\n", " ")
	    print(out)
	    print()