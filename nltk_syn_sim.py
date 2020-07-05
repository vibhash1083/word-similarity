from nltk.corpus import wordnet as wn
from utils import timeit


def generate_similar_words(word, lch_threshold=2.5):
    for net1 in wn.synsets(word):
        for net2 in wn.all_synsets():
            try:
                lch = net1.lch_similarity(net2)
            except:
                continue
            if lch >= lch_threshold and net1.lemmas()[0].name() == word:
                yield (net1.lemmas()[0].name(), net2.lemmas()[0].name(), lch, net1.topic_domains())


@timeit
def generate_synonyms(word):
    synonyms = set()
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
    return synonyms


@timeit
def prepare_similar_words_set(word):
    similar_words = set()
    for x in generate_similar_words(word):
        similar_words.add(x[1])
    return similar_words


word = input("Enter your word: ")
print(generate_synonyms(word))
print(prepare_similar_words_set(word))
