PRACTICAL TALK: LARGE-SCALE LANGUAGE GROUNDING WITH VISION: (YEJIN CHOI)
=======================================================================

- Generating images: problem _what can be described by human_ (image labels) and _what can be recognised_ (what's in the image - basic stuff) is not the same
- Why to describe images?
    - summarize photo album
    - advance usage: guess intend of participants

Pipeline
--------
* identify objects
* come up with properties
    - unary
        - object
        - attribute
        - proposition
    - binary
        - object - atribute - value
        - proposition - object - atribute - value  // something like speech act?
* Come up with relevant NP (subtrees)
* Use CRF see below


Using CRF
---------
- baseline: traverse the graph and use templates (rigid, funny, but somehow works)
- how to combine fragments of dependency parse tree to sensible output (nlg problem)
    - compute similarity between fragments
    - see how the object (image) was described in different settings
    - using ILP (Integer Linear Programming)
        - Content selection score - pick what to inform about from dialogue state
        - PCFG
        - LM
    - over generating  too detail information like dates (hallucinating)
        - solution: prunning
            - discards what is not so relevant and more fluent (favor style over semantics)
            - _my idea_: if high uncertainty produce shorter sentences (not that many non sensical mistakes)

