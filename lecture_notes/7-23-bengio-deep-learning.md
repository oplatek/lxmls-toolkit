Deep learning (Yoshua Bengio)
=============================

Generating captions from image
------------------------------
- Attention  mechanism
    - Bahdanau, Cho, Bengio machine translation - **LOOK AT IT**
    - also used for memory **TODO**
- **memory networks, neural turing machines Graves at al 2014, Weston et al 2014**
    - memory networks are like associate dictionaries
        - embedgings - they are very exact

Remarks
-------
- Use of embeddings
    - train two functions $$\Phi-words$$ and $$\Phi-image$$ to produce embeddings in the same space
        - image with the same meaning - the two functions (for image and the words) should output close embedings
        - training should move not similar things from each other - otherwise it will collapse to single point;-)
- Smoothness prior - the default prior $$y-unseen = f(x-unseen) + \epsilon$$
    - it is not enough for high dimensions
    - **theorem**: it is not enough for perturbed sine function f-x - e.g. Gaussian kernels machine needs k parameters if f-x has 2k crossing the x access
    - we **something better:**
        - **Compositionality is useful to describe the world around use efficiently.**
            - distributional semantics
            - multiple levels of feature learning
- embeddings - LM
    - the biggest clusters - POS - most common structure
    - zooming in - smaller clusters of semantic
    - **how to use it?**
        - Mikolov use it for semantic representation
    - embeddings are learning the bunch of attributes and mapping different sets of attributes to different places
        - **TODO train attributes and discover which regions**
    - embeddings LM - how do they deal with embeddings - TODO see Babelnet paper


- Adversial Nerual nets - use it for text generation
    - TODO find article
    - Discriminator and Generator adapt very frequently in a loop

 
