import random

# Code for Quicksort
def partition(a, lo, hi, p_index):
    """Decides on the pivot index based on the p_index parameter and partitions the array."""
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

def quick_sort(a, p_index = "random"):
    """Sorts the array in place using the quicksort algorithm."""
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

# Code for Mergesort
def merge_sort(a):
    """Sorts the array in place using the mergesort algorithm."""
    n = len(a)
    if n < 2:
        return
    buf = [None] * n
    def merge(lo, mid, hi):
        buf[lo:hi + 1] = a[lo:hi + 1]
        i, j = lo, mid + 1

        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = buf[j]; j += 1
            elif j > hi:
                a[k] = buf[i];i += 1
            elif buf[j] < buf[i]:
                a[k] = buf[j]; j += 1
            else:
                a[k] = buf[i]; i += 1

    def sort(lo, hi):
        """Recursively sorts the array using the mergesort algorithm."""
        if  lo >=hi:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid + 1, hi)
        merge(lo, mid, hi)
    sort(0, n - 1)