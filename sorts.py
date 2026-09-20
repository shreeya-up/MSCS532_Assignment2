import random

# Code for Quicksort
def partition(a, lo, hi, p_index):
    if p_index == "random":
        m = random.randint(lo, hi)
    elif p_index == "first":
        m = lo
    elif p_index == "median3":
        mid = (lo + hi) // 2
        m = sorted((lo, mid, hi), key=lambda i: a[i])[1]
    else:
        m = hi
    a[m], a[hi] = a[hi], a[m]
    x = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[hi] = a[hi], a[i + 1]
    return i + 1

def quicksort(a, p_index = "random"):
    def sort(lo, hi):
        while lo<hi:
            q = partition(a, lo, hi, p_index)
            if q - lo < hi - q:
                sort(lo, q - 1)
                lo = q + 1
            else:
                sort(q + 1, hi)
                hi = q - 1
    sort(0, len(a) - 1)