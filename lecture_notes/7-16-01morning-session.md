<!-- Hack for introducing math - should not work on Github -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

Review of Probability Theory
==============================================

Morning session July 16.
Afternoon labs are in building 9.

Dictionary Cz-En
----------------
- Probability mass function - pravdepodobnostni funkce (for discrete)
- Density function - hustota (for continuous)
- Cumulative distribution function - distribucni funkce (the same name for continuous and discrete)
- False alarms
- False positive

**TODO understand Poisson distribution**

Nice indicator trick: If I want to know probability of $$x \in A$$, I may to introduce indicator function $$1_A(x)$$ where 
$$1_A(x) = 1 \iff  x \in A $$
$$1_A(x) = 0 \iff  x \notin A $$

From the equation of Expected value 
$$ \mathbf{E}(x) = \int_{-\inf}^{\inf} x * f_X(x) d x $$ 
and 
$$ \mathbf{E}(g(x)) = \int_{-\inf}^{\inf} g(x) * f_X(x) d x $$
we can simply write

$$P(x \in A) = \int_A f_X(x) dx = \int 1_A(x) f_X(x) d x = \mathbf{E}(1_A(x)) $$

TODO go through slides 34 and more

Recommended reading
-------------------
- K. Murphy "Machine Learning: A probabilistic perspective", MIT
- L. Wasserman "All of statistics: Concise Course
