Deep learning (Yoshua Bengio)
=============================

Generating captions from image
------------------------------


Remarks
-------
- Use of embeddings
    - train two functions $$\Phi-words$$ and $$\Phi-image$$ to produce embeddings in the same space
        - image with the same meaning - the two functions (for image and the words) should output close embedings
        - training should move not similar things from each other - otherwise it will collapse to single point;-)
- Smoothness prior - the default prior $$y-unseen = f(x-unseen) + \epsilon$$
    - it is not enough for high dimensions
    - it is not enough for perturbed sine function f-x - e.g. Gaussian kernels needs k parameters if f-x has k crossing the x access
