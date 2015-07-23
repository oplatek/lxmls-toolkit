Meaning in the wild - Fernando Pereira
======================================

Random remarks
-------------
- dependency parsing is good start point for efficient natural language understanding (NLU)
- one would like RDFify all the web pages so one would be able to travel all the web pages through all the name entities in the websites
- One entity has many types according context
    - Obama is a president(0.8), Obama is an author (0.2)
    - important to work with priors e.g 0.8 and 0.2 for Obama
    - since the people are working with them if they say nothing they assume their prior
    - **On the other hand, if a person is using a word during article/utterance/conversation it is typically used in one sense**
        - **if the conversation is a metadiscussion about the word meaning itself**
- **SLU** needs **very few information from context only a few!**
    - too much information/too broad context is misleading
- balance between **memory and inference**
    - current models do not memorize large number of facts
        - word embedings are good way for that 
            - I am able to represent tons of words, if I do not know I pass UNKK
            - I may rely on other than lexical features from my word
            - TODO prefer words if I need them
                - solution **embedings with posteriors**?
                    - Gaussion embedings? http://arxiv.org/pdf/1412.6623v4.pdf
- current state of the art: **Good results only with labeled data**
- **Speech is more syntactic than chat**
    - we do not speak in keywords
    - it is good to have prior for filling in grammar
        - if I say: "Malostranske namesti, Andel"
            - I mean: "Please, find me a connection from Malostranskeho namesti to Andel"
                - **TODO pass e.g to NN a score of gramaticality and when asking for representation of intention "request(Andel, Malostranska" the most grammatical salient feature should be "Please, find me a connection from Malostranskeho namesti to Andle"

Attention based models
----------------------
- attention based models
    - the way to go
    - features from KB surrounding (trained on domain texts and only used in looking in the KB node neighborhood (F. Pereira work - TODO citation)
    - voting features based on their performance
        - still very sparse features - very few indicators is needed see (random remarks)
    - recommended reading: Random Walk Inference and Learning in A Large Scale Knowledge Base (http://www.cs.cmu.edu/~tom/pubs/lao-emnlp11.pdf)
    - KB can be used as **light supervision**
        - and only as light supervision for **matching between KB <-> and Deep parsing**
            - path (Mention, conj, Mention^{-1}, Prefesion)
                - is either too specific or too general

Ontologies as abstraction?
--------------------------
- current ontologies e.g. schema.org are very sparse, and not intuitive for people 
    - people do not abstract according schema.org
        - framenet may be better or even Wordnet?
    - in order to traverse ontologies one should find much more dimension to traverse them than through current ontologies
- ontologies may be used as priors
    - many different ontologies should be combines for priors
- linguistic frames are also ontologies
