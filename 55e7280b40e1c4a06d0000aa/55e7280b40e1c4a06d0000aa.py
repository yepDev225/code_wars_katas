from itertools import combinations
def choose_best_sum(t, k, ls):
    best =0
    for comb in combinations(ls, k):
        total = sum(comb)
        if total <= t:
            best = max(best, total)
    return best if best > 0 else None