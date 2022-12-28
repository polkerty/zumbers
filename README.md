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

#### Increase all values in a spectrum by 1
This can be achieved most easily by adding a 0 to the original zumber. 

