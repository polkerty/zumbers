from zumber import check, nth_two_star_zumber

'''
Commands
'''
# ans = tuple(sorted(sub_zumbers_of_multiset(nth_symmetric_zumber(3), set())))
# ans2 = tuple(sorted(sub_zumbers_of_multiset2(nth_symmetric_zumber(10))))
# print(ans)
# print(ans2)
# print(ans == ans2)

# factor_symmetric_zumbers(11)

# search(lambda: random_zumber(18, 9), count=5, print_spectra=True)
# search(
#     # lambda: mutate_zumber(nth_two_star_zumber(4), changes=10, deltas=[-3, -2, -1, 1, 2, 4]),
#     lambda: random_zumber(10, 10),
#     count=10000,
#     print_spectra=True,
# )
# filter_spectrum=(3, 4, 5))

# check(nth_two_star_zumber(4))
# check((-64, -32, -16, -8, -4, -2, -1, -8, 8, 1, 2, 4, 8, 16, 32, 64))
# filter_rule=lambda z, s: len(s) > 2)
# check((-7, -7, -7, -9, 10, 10, 10, -10, -10, -1, 7, 7, 7))
# check((-7, -7, -7, -7, -11, 13, 13, 13, -13, -13, -2, 7, 7, 7, 7))
for n in range(3, 13):
    check(nth_two_star_zumber(n))

# check((-1, -1, -1, -1, -1, -1, 6, -6, 1, 1, 1, 1, 1, 1))
# check((-1, -1, -1, 3, -6, 6, -3, 1, 1, 1))
