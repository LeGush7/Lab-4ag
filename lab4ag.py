from itertools import combinations


# sp - survival points
# pin - place in bag
START_SP = 20
MAX_PIN = 8
NEED_LOOT = 'i'
loot = {
    'r': (3, 25), 'p': (2, 15), 'a': (2, 15), 'm': (2, 20), 'i': (1, 5),
    'k': (1, 15), 'x': (3, 20), 't': (1, 25), 'f': (1, 15), 'd': (1, 10),
    's': (2, 20), 'c': (2, 20)
}


def result_sp(choosen_loot):
    total_pin = sum([loot[item][0] for item in choosen_loot])
    total_sp = sum([loot[item][1] for item in choosen_loot])\
               + START_SP - sum([loot[item][1] for item in loot
                                 if item not in choosen_loot])
    return total_pin, total_sp


biggest_sp = -10000
best_comb = ()
for x in range(1, len(loot) + 1):
    for comb in combinations(loot.keys(), x):
        if NEED_LOOT in comb:
            total_pin, total_sp = result_sp(comb)
            if MAX_PIN >= total_pin and total_sp > biggest_sp:
                biggest_sp = total_sp
                best_comb = comb

best_comb_bag = []
for item in best_comb:
    for x in range(loot.get(item)[0]):
        best_comb_bag.append(item * loot.get(item)[0])
lines = [best_comb_bag[:4], best_comb_bag[4:]]
for line in lines:
    print(",".join(f"[{item[0]}]" for item in line))
print("Итоговые очки выживания:", biggest_sp)
