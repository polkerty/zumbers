def is_zumber(nums):
    return sum(nums) == 0


def canonical_form(zumber):
    return tuple(sorted(list(zumber)))


subset_cache = dict()


def sub_zumbers_of_multiset2(multiset):
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


def divide(parent, child):
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


prime_cache = dict()


def prime_factors_of_zumber(zumber):
    if zumber in prime_cache:
        # print(zumber, len(prime_cache))
        return prime_cache[zumber]
    ans = [z for z in sub_zumbers_of_multiset2(zumber, ) if is_prime(z)]
    prime_cache[zumber] = ans
    return ans


is_prime_cache = dict()


def is_prime(zumber):
    if zumber in is_prime_cache:
        return is_prime_cache[zumber]

    is_prime_cache[zumber] = len(sub_zumbers_of_multiset2(zumber)) == 1
    return is_prime_cache[zumber]


def spectrum(zumber, seen):
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


def nth_symmetric_zumber(n):
    ret = []
    for i in range(1, n + 1):
        ret.extend([i, -i])
    return canonical_form(ret)


def factor_symmetric_zumbers(max=20):
    cache = dict()
    for n in range(1, max + 1):
        z = nth_symmetric_zumber(n)
        s = spectrum(z, cache)
        print(n, ": ", z, ":", tuple(sorted(list(s.keys()))))
        for (n, example) in sorted(s.items()):
            print('\t', n, ': ', example)


import random

# random.seed('love')
random.seed('love2')


def random_zumber(size=5, window=5):
    nums = []
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


def mutate_zumber(z, changes=1, deltas=tuple([-1, 1])):
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


def nth_two_star_zumber(n):
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


def search(generator, count=100, print_spectra=False, filter_spectrum=None, filter_rule=None):
    cache = dict()
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


def check(z):
    cache = dict()
    # z = (-7, -7, -7, -7, -5, -5, -4, -4, -4, 4, 5, 7, 34)
    # z = canonical_form((-8, -8, -5, 7, 7, 7, -7, -7, -2, 8, 8))
    z = canonical_form(z)
    print(z)
    print(tuple(sorted(list(spectrum(z, cache).keys()))))
    for (n, example) in sorted(spectrum(z, cache).items()):
        print('\t', n, ': ', example)
    # z2 = canonical_form((-11, -11, 4, 6, 6, 6, -6, -6, -10, 11, 11))
    # print(z2)
    # print(tuple(sorted(list(spectrum(z2, cache).keys()))))
    # for (n, example) in sorted(spectrum(z2, cache).items()):
    #     print('\t', n, ': ', example)


if __name__ == '__main__':
    # ans = tuple(sorted(sub_zumbers_of_multiset(nth_symmetric_zumber(3), set())))
    # ans2 = tuple(sorted(sub_zumbers_of_multiset2(nth_symmetric_zumber(10))))
    # print(ans)
    # print(ans2)
    # print(ans == ans2)

    # factor_symmetric_zumbers(11)

    # search(lambda: random_zumber(11, 9))
    # search(
    #     # lambda: mutate_zumber(nth_two_star_zumber(4), changes=10, deltas=[-3, -2, -1, 1, 2, 4]),
    #     lambda: random_zumber(10, 10),
    #     count=10000,
    #     print_spectra=True,
    # )
    # filter_spectrum=(3, 4, 5))

    # check(nth_two_star_zumber(4))
    check((-32, -16, -4, -2, -1, -1, 1, 1, 2, 4, 16, 32))
    # filter_rule=lambda z, s: len(s) > 2)
    # check((-7, -7, -7, -9, 10, 10, 10, -10, -10, -1, 7, 7, 7))
    # check((-7, -7, -7, -7, -11, 13, 13, 13, -13, -13, -2, 7, 7, 7, 7))
    # for n in range(3, 12):
    #     check(nth_two_star_zumber(n))
