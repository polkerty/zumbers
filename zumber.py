Zumber = tuple[int, ...]
from typing import Union, Callable, Optional


def is_zumber(nums: Zumber):
    return sum(nums) == 0


def canonical_form(zumber: Union[Zumber, list[int]]):
    return tuple(sorted(list(zumber)))


subset_cache: dict[Zumber, list[Zumber]] = dict()


def sub_zumbers_of_multiset2(multiset: Zumber):
    if multiset in subset_cache:
        return subset_cache[multiset]
    ret = []
    for i in range(1, 2 ** len(multiset)):
        item = []
        tot = 0
        for j in range(len(multiset)):
            if i & (1 << j):
                item.append(multiset[j])
                tot += multiset[j]
        if tot == 0:
            ret.append(tuple(item))

    subset_cache[multiset] = ret
    return ret


def divide(parent: Zumber, child: Zumber):
    totals = {}
    for x in parent:
        if x not in totals:
            totals[x] = 1
        else:
            totals[x] += 1

    for x in child:
        if x not in totals or totals[x] == 0:
            raise ValueError(f"{parent} is not a parent of {child}")
        totals[x] -= 1

    complement = []
    for (n, c) in totals.items():
        complement += [n] * c

    return canonical_form(complement)


prime_cache: dict[Zumber, list[Zumber]] = dict()


def prime_factors_of_zumber(zumber):
    if zumber in prime_cache:
        # print(zumber, len(prime_cache))
        return prime_cache[zumber]
    ans = [z for z in sub_zumbers_of_multiset2(zumber, ) if is_prime(z)]
    prime_cache[zumber] = ans
    return ans


is_prime_cache: dict[Zumber, bool] = dict()


def is_prime(zumber: Zumber):
    if zumber in is_prime_cache:
        return is_prime_cache[zumber]

    is_prime_cache[zumber] = len(sub_zumbers_of_multiset2(zumber)) == 1
    return is_prime_cache[zumber]


Spectrum = dict[int, list[Zumber]]
SpectrumCache = dict[Zumber, Spectrum]


def spectrum(zumber: Zumber, seen: SpectrumCache):
    if zumber in seen:
        return seen[zumber]
    prime_factors = prime_factors_of_zumber(zumber)

    spec = dict()

    for p in prime_factors:
        if p == zumber:
            spec[1] = [zumber]
            continue
        complement = divide(zumber, p)
        child_spectrum = spectrum(complement, seen)
        for s, example in child_spectrum.items():
            if s + 1 not in spec:
                spec[s + 1] = [p] + example

    # s = tuple(sorted(list(spec)))
    seen[zumber] = spec
    return spec


def nth_symmetric_zumber(n: int):
    ret = []
    for i in range(1, n + 1):
        ret.extend([i, -i])
    return canonical_form(ret)


def factor_symmetric_zumbers(max: int = 20):
    cache: SpectrumCache = dict()
    for n in range(1, max + 1):
        z = nth_symmetric_zumber(n)
        s = spectrum(z, cache)
        print(n, ": ", z, ":", tuple(sorted(list(s.keys()))))
        for (n, example) in sorted(s.items()):
            print('\t', n, ': ', example)


import random

# random.seed('love')
random.seed('love2')


def random_zumber(size: int = 5, window: int = 5):
    nums: list[int] = []
    while len(nums) < size - 1:
        num = random.randint(-window, window)
        if num == 0:
            continue
        nums.append(num)
    inv = -sum(nums)
    if inv == 0:
        return random_zumber(size, window)
    nums.append(inv)
    return canonical_form(nums)


def mutate_zumber(z: Zumber, changes=1, deltas=tuple([-1, 1])):
    ret = canonical_form(z)  # also makes into a tuple
    for _ in range(changes):
        pos1 = random.randint(0, len(z) - 1)
        pos2 = random.randint(0, len(z) - 1)
        while pos1 == pos2:
            pos2 = random.randint(0, len(z) - 1)
        pos1, pos2 = min(pos1, pos2), max(pos1, pos2)
        change = random.choice(deltas)

        # We need change another position by the exact opposite of the amount we changed this position
        # in order to balance things out.
        ret = ret[:pos1] + (ret[pos1] + change,) + ret[pos1 + 1:pos2] + (ret[pos2] - change,) + ret[pos2 + 1:]
    return canonical_form(ret)


def nth_two_star_zumber(n: int):
    if n < 3:
        raise ValueError('N should be 5 or higher')
    '''
        C - A - D = 0
        3C - 6B - A = 0
    '''
    b = 5
    a_base = 5
    a = a_base + (3 - (((n - 3) * b + a_base) % 3))
    c = ((n - 3) * b + a) // 3
    d = c - a

    return canonical_form([b] * (n - 3) + [-a, c, c, c, -c, -c, -d] + [-b] * (n - 3))


def search(generator: Callable[[], Zumber], count: int = 100, print_spectra: bool = False,
           filter_spectrum: Union[None, tuple[int, ...]] = None,
           filter_rule: Optional[Callable[[Zumber, Spectrum], bool]] = None):
    cache: SpectrumCache = dict()
    passed = 0
    by_spectra = dict()
    for n in range(count):
        z = generator()
        if not is_zumber(z):
            raise ValueError("Generator yielded a non-zumber: ", z)
        s = spectrum(z, cache)
        sl = sorted(list(s))
        normalized_spectrum = tuple(sorted(list(s.keys())))
        if filter_rule and not filter_rule(z, s):
            continue
        if filter_spectrum and filter_spectrum != normalized_spectrum:
            continue
        passed += 1
        if not normalized_spectrum in by_spectra:
            by_spectra[normalized_spectrum] = 1
        else:
            by_spectra[normalized_spectrum] += 1
        # if len(sl) < 2:
        #     continue
        # gap = max([b - a for (a, b) in zip([0] + sl, sl)])
        # gap = max([b - a for (a, b) in zip(sl, sl[1:])])
        # if gap < 3:
        #     continue
        print(f'{n}\t', ":", z, "\t:", normalized_spectrum)
        if print_spectra:
            for (n, example) in sorted(s.items()):
                print('\t', n, ': ', example)
    print(f"Total passes: {passed}/{count} ({passed / count * 100:.02f}%)")
    print("Spectrum stats:")
    for (s, c) in sorted(by_spectra.items()):
        print(f"{s}:\t", c, f"\t({c / passed * 100:.02f}%)")


def check(z: Zumber):
    if not is_zumber(z):
        raise ValueError("This is not a zumber: ", z)

    cache: SpectrumCache = dict()
    # z = (-7, -7, -7, -7, -5, -5, -4, -4, -4, 4, 5, 7, 34)
    # z = canonical_form((-8, -8, -5, 7, 7, 7, -7, -7, -2, 8, 8))
    z = canonical_form(z)
    print(z, f'[{len(z)}]')
    print(tuple(sorted(list(spectrum(z, cache).keys()))))
    for (n, example) in sorted(spectrum(z, cache).items()):
        print('\t', n, ': ', example)
    # z2 = canonical_form((-11, -11, 4, 6, 6, 6, -6, -6, -10, 11, 11))
    # print(z2)
    # print(tuple(sorted(list(spectrum(z2, cache).keys()))))
    # for (n, example) in sorted(spectrum(z2, cache).items()):
    #     print('\t', n, ': ', example)


def gen_triplet(a: int, b: int, c: int):
    smallest = min(a, b, c)
    zero_count = smallest - 2
    (x, y, z) = tuple(sorted((a - zero_count, b - zero_count, c - zero_count)))
    one_count = z - 2
    mid_val = z - y + 1
    last_val = one_count + mid_val

    return (0,) * zero_count + (1,) * one_count + (-1,) * one_count + (mid_val, -mid_val, last_val, -last_val)
