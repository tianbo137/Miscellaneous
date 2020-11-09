# Benford's law 

A remarkable phenomenon in probability theory is that of universality, that many seemingly unrelated probability distributions, which involve large numbers of unknown parameters, can end up converging to a universal law that may only depend on a small handful of parameters. One of the most famous examples of the universality phenomenon is the central limit theorem; Another such universality phenomena show up in the distributions of a statistic X from a large population of “real-world” objects. That is,

_**Benford's law: for {d = 1,...,9}, the probability of X with first digit d is approximately**_:

<p align="center">
  <img src="https://github.com/tianbo137/benford_law_check/blob/main/26461e7841d135d327aa7d0f914236862e890e7b.png">
</p>

For instance, {X} should have a first digit of 1 about 30.1% of the time, but a first digit of 9 only about 5% of the time, see the following:
<p align="center">
  <img src="https://github.com/tianbo137/benford_law_check/blob/main/0*aEKtSyYHDtAZ5Crq.gif">
</p>

Of course, in order for Benford's law to be valid, the following assumptions should be satisfied:
1. take values as positive numbers;
2. range over many different orders of magnitude;
3. arise from a complicated combination of largely independent factors (with different samples of {X} arising from different independent factors); and
4. have not been artificially rounded, truncated, or otherwise constrained in size.

An extensive discussion of the origin, rigorous proof, and applications of Benford's law is beyond the scope of this note, and we refer the interested reader to https://en.wikipedia.org/wiki/Benford%27s_law and https://www.ams.org/journals/notices/201702/rnoti-p132.pdf for more details and references therein. Our goal here is to implement a small module to check if any given dataset in csv format satisfies the Benford's law or not via the Chi-squared test (https://en.wikipedia.org/wiki/Chi-squared_test).
