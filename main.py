from zumber import check, nth_two_star_zumber, search, random_zumber, mutate_zumber, gen_triplet, \
    gen_zumber_with_spectrum

if __name__ == '__main__':
    # ans = tuple(sorted(sub_zumbers_of_multiset(nth_symmetric_zumber(3), set())))
    # ans2 = tuple(sorted(sub_zumbers_of_multiset2(nth_symmetric_zumber(10))))
    # print(ans)
    # print(ans2)
    # print(ans == ans2)

    # factor_symmetric_zumbers(11)

    # search(lambda: random_zumber(14, 10), count=1000, print_spectra=True)
    # search(
    #     lambda: mutate_zumber((-10, -10, -7, -3, -2, -2, -2, 2, 2, 5, 5, 7, 7, 8), changes=10,
    #                           deltas=[-3, -2, -1, 1, 2, 4]),
    #     # lambda: random_zumber(10, 10),
    #     count=10000,
    #     print_spectra=True,
    # )
    # filter_spectrum=(3, 4, 5))

    # check(nth_two_star_zumber(4))
    # check((-64, -32, -16, -8, -4, -2, -1, -8, 8, 1, 2, 4, 8, 16, 32, 64))
    # filter_rule=lambda z, s: len(s) > 2)
    # check((-7, -7, -7, -9, 10, 10, 10, -10, -10, -1, 7, 7, 7))
    # check((-7, -7, -7, -7, -11, 13, 13, 13, -13, -13, -2, 7, 7, 7, 7))
    # for n in range(3, 13):
    #     check(nth_two_star_zumber(n))

    # check((3, 3, 3, 3, 3, -3, -3, -3, -3, -3, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 30))
    # check((3, 3, 3, 3, 3, -3, -3, -3, -3, -3, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 30))
    # check((-1, -1, -1, 3, -6, 6, -3, 1, 1, 1))
    # check((-1, -1, -1, -1, 4, -1, -1, -1, -1, -1, 9, 1, 1, 1, 1, -4, 1, 1, 1, 1, 1, -9))
    # check((-1, -1, -1, -1, 4, -17, -17, -17, -17, -17, 85, 1, 1, 1, 1, -4, 17, 17, 17, 17, 17, -85))
    # check((-1, -1, -1, -1, -17, -17, -17, -17, -17, 19, 108, 1, 1, 1, 1, 17, 17, 17, 17, 17, -19, -108))
    # check((-1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6, -15))

    # check(gen_triplet(3, 4, 11))
    # check(gen_triplet(3, 5, 11))
    # check(gen_triplet(3, 6, 11))
    # check(gen_triplet(3, 7, 11))
    # check(gen_triplet(3, 8, 11))
    # check(gen_triplet(3, 9, 11))

    # check((-1,) * 10 + (1,) * 10 + (4, 11, 21, -21, -11, -4))
    # seq = (6, 9, 10)   (6 -1 - 1s === 5) (9 -2 -1s + 6 === 13) (10 - 3 1's + 13 = 20

    # check(gen_zumber_with_spectrum((2, 6, 9, 10, 12)))
    check(gen_zumber_with_spectrum((4, 7, 10, 12)))
    check(gen_zumber_with_spectrum((3, 9, 10)))
    check(gen_zumber_with_spectrum((2, 3, 6, 8, 9)))
