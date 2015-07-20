Structured prediction
=====================
Point of view: It is easier to  over generate features (e.g. using template feature functions) and use machine learning (convenient learning algorithm) which will pick the relevant features.

**Generative models are simple but need smoothing and smoothing is black magic.**

$$f(x, i, l)$$ represent an assignment of label x for x_i
    - features for position i and label l
    - such feature function is limited to looking to input context (may not be enough)
    - it would be beneficial to also look to surrounding predicted labels

HMMs is a structured predictor because there the transitional probabilities 
    $$P_{X,Y}$$.
On the other hand, the observation probabilities
    $$P(O|S)$$
are very summarizing but cannot express structured feature functions.



Conditional Random Fields(CRF)
==============================
See the slides
