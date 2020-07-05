# Synonyms and semantically similar words

Script and service to generate synonyms and similar words for a given word using python [NLTK library](https://www.nltk.org/) and [WordNet](https://wordnet.princeton.edu/) database.

## Installation
This project requires [Python 3](3https://www.python.org/downloads/).

Set up Python path.

Download and install pip
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Install [virtualenv](https://virtualenv.pypa.io/en/stable/), create and activate virtual environment
```sh
pip install virtualenv
virtualenv <name_of_env>
source <name_of_env>/bin/activate
```

Clone repository and install dependencies
```sh
pip install -r requirements.txt
```

Download WordNet database by executing following commands in python shell (enter python in terminal)
```
import nltk
nltk.download('wordnet')
```

Execute script
```sh
python nltk_syn_sim.py
```

To use same as service
```sh
python synonym_service.py
```

Send a GET request to the URL - ```http://0.0.0.0:8000/word/<input_word>/```

## NLTK WordNet similarity metrics

NLTK provides two groups of similarity metrics
1. Thesaurus based metrics
    1. Path similarity
    2. Leacock-Chodorow Similarity
    3. Wu-Palmer Similarity
2. Thesaurus and probabilistic information from distributions in corpora based metrics
    1. Resnik Similarity
    2. Lin Similarity
    3. Jiang-Conrath distance

WordNet is a graph of words and path similarity approach shortest path from one word sense to another word sense.
Leacock-Chodorow Similarity, which we are using in these scripts, gives negative logarithm of result of path similarity.

### From WordNet:
https://www.nltk.org/howto/wordnet.html

> synset1.lch_similarity(synset2): Leacock-Chodorow Similarity: Return a score denoting how similar two word senses are, based on the shortest path that connects the senses (as above) and the maximum depth of the taxonomy in which the senses occur. The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.

## Examples
To be added

## Ehnacements
Explore feasibility of domain based matches using [WordNet Domains](http://wndomains.fbk.eu/hierarchy.html)
