# Zumbers
A zumber is a multiset of reals with sum 0. The sum of two zumbers is the union of their elements.
A factorization of a zumber breaks it down into two or more zumbers that can be added to 
get the original zumber.
A zumber is "prime" if it cannot be factored.
A prime factorization is a factorization where all factors are primes. Factorization is
not unique.

## Spectrum
The spectrum of a zumber is the list of different lengths of **prime** factorizations for that zumber. For example,
the following zumber has both a 2-factorization and a 3-factorization, so its spectrum is (2, 3):

> (-3, -2, -1, 1, 2, 3) has a 3-factorization: (-3, 3), (-2, 2), (-1, 1) and a 2-factorization: (-3, 2, 1), (1, 2, -3).


### Generating zumber spectra
In general, it is thought that all theoretically possible spectra exist. That is,
any monotonically increasing list (x<sub>1</sub>, x<sub>2</sub>, ...)
where the x<sub>i</sub> integers greater than 1, corresponds to one or more zumbers.

We do not have a general proof of this yet, but there is some progress

#### Trick 1: Increase all values in a spectrum by 1
This can be achieved most easily by adding a 0 to the original zumber. 


### Trick 2: Generate spectra of the form (2, n)
Pick two numbers a, b that are relatively prime.



#### [old]  Generate spectra of the form (2, n) (n ≥ 3)
The following technique works for most values of (A, B, N):

Fix integers A and B. Generate C, D according to the following rules:

```
        3A - (N-3)B = C
        A - C  = D
```

Then generate a zumber with the following pattern:

(-A, -A, ... -A) (N-3 times) + [-C, B, B, B, -B, -B, -D] + (A, A, ... A) (N - 3 times).

(For some small values of A, for instance, the spectrum may contain some additional
"ghost" values.)

The following shows possible zumbers for (2, 3) through (2, 10), along with their 
spectra and an example factorization for each spectrum:

```
(-6, -2, -2, 2, 2, 2, 4)
(2, 3)
	 2 :  [(-6, 2, 2, 2), (-2, -2, 4)]
	 3 :  [(-2, 2), (-2, 2), (-6, 2, 4)]
(-7, -5, -4, -4, 3, 4, 4, 4, 5)
(2, 4)
	 2 :  [(-7, -5, 4, 4, 4), (-4, -4, 3, 5)]
	 4 :  [(-4, 4), (-4, 4), (-7, 3, 4), (-5, 5)]
(-8, -6, -6, -5, -5, 2, 5, 5, 6, 6, 6)
(2, 5)
	 2 :  [(-6, -6, 2, 5, 5), (-8, -5, -5, 6, 6, 6)]
	 5 :  [(-5, 5), (-5, 5), (-6, 6), (-6, 6), (-8, 2, 6)]
(-7, -7, -6, -5, -5, -5, -1, 5, 5, 5, 7, 7, 7)
(2, 6)
	 2 :  [(-7, -7, -1, 5, 5, 5), (-6, -5, -5, -5, 7, 7, 7)]
	 6 :  [(-5, 5), (-5, 5), (-5, 5), (-7, 7), (-7, 7), (-6, -1, 7)]
(-9, -9, -7, -5, -5, -5, -5, -2, 5, 5, 5, 5, 9, 9, 9)
(2, 7)
	 2 :  [(-9, -9, -2, 5, 5, 5, 5), (-7, -5, -5, -5, -5, 9, 9, 9)]
	 7 :  [(-5, 5), (-5, 5), (-5, 5), (-5, 5), (-9, 9), (-9, 9), (-7, -2, 9)]
(-11, -11, -8, -5, -5, -5, -5, -5, -3, 5, 5, 5, 5, 5, 11, 11, 11)
(2, 8)
	 2 :  [(-11, -11, -3, 5, 5, 5, 5, 5), (-8, -5, -5, -5, -5, -5, 11, 11, 11)]
	 8 :  [(-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-11, 11), (-11, 11), (-8, -3, 11)]
(-12, -12, -6, -6, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 12, 12, 12)
(2, 9)
	 2 :  [(-12, -12, -6, 5, 5, 5, 5, 5, 5), (-6, -5, -5, -5, -5, -5, -5, 12, 12, 12)]
	 9 :  [(-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-12, 12), (-12, 12), (-6, -6, 12)]
(-14, -14, -7, -7, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 14, 14, 14)
(2, 10)
	 2 :  [(-14, -14, -7, 5, 5, 5, 5, 5, 5, 5), (-7, -5, -5, -5, -5, -5, -5, -5, 14, 14, 14)]
	 10 :  [(-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-14, 14), (-14, 14), (-7, -7, 14)]
```

This technique introduces two common tricks:
- Split positive/negative pairs of numbers into different factors in one factorization, but pair them in another 
factorization with more terms.
- Introduce indefinitely many terms into a 2-factorization by requiring a large number of small terms
to cancel out with a small number of large terms. Removing any of the small terms from the factorization
automatically forces you to remove SEVERAL small terms, because they were all being cancelled out by the same
large factor. This technique allows us to "bump" across gaps in a spectra.

Also, note that when paired with Trick 1, we can now generate zumbers for 
any spectra of the form (M, N).