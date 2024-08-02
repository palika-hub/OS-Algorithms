from queue import Queue

def FIFO(pages, n, capacity):

    s = set()

    indexes = Queue()

    page_faults = 0
    page_hits = 0 

    for i in range(n):

        if len(s) < capacity:

            if pages[i] not in s:
                s.add(pages[i])

                page_faults += 1

                indexes.put(pages[i])

            else:
                page_hits += 1

        else:

            if pages[i] not in s:

                val = indexes.queue[0]
                indexes.get()

                s.remove(val)

                s.add(pages[i])

                indexes.put(pages[i])

                page_faults += 1

            else:
                page_hits += 1

    hit_ratio = page_hits / n
    miss_ratio = 1 - hit_ratio

    return page_faults, page_hits, hit_ratio, miss_ratio


def LRU(pages, n, capacity):
    s = set()
    indexes = {}
    page_faults = 0
    page_hits = 0  # Initialize page hits

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
        else:
            if pages[i] not in s:
                lru = float('inf')
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page
                s.remove(val)
                s.add(pages[i])
                page_faults += 1
            else:
                page_hits += 1  
            indexes[pages[i]] = i

    hit_ratio = page_hits / n
    miss_ratio = 1 - hit_ratio 

    return page_faults, page_hits, hit_ratio, miss_ratio


def MRU(pages, n, capacity):
    s = set()
    indexes = {}
    page_faults = 0
    page_hits = 0  # Initialize page hits

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
        else:
            if pages[i] not in s:
                mru = -1
                for page in s:
                    if indexes[page] > mru:
                        mru = indexes[page]
                        val = page
                s.remove(val)
                s.add(pages[i])
                page_faults += 1
            else:
                page_hits += 1  # Page is found in the set
            indexes[pages[i]] = i

    hit_ratio = page_hits / n
    miss_ratio = 1 - hit_ratio 

    return page_faults, page_hits, hit_ratio, miss_ratio


def search(key, fr):
    for i in range(len(fr)):
        if (fr[i] == key):
            return True
    return False
 
def predict(pg, fr, pn, index):
    res = -1
    farthest = index
    for i in range(len(fr)):
        j = 0
        for j in range(index, pn):
            if (fr[i] == pg[j]):
                if (j > farthest):
                    farthest = j
                    res = i
                break
        if (j == pn):
            return i
    return 0 if (res == -1) else res

def OptimalPage(pages, n, capacity):  
    fr = []
    page_hits = 0
    page_faults = 0

    for i in range(n):
        if search(pages[i], fr):
            page_hits += 1
        else:
            page_faults += 1

            if len(fr) < capacity:
                fr.append(pages[i])
            else:
                j = predict(pages, fr, n, i + 1)
                fr[j] = pages[i]

    hit_ratio = page_hits / n
    miss_ratio = 1 - hit_ratio 

    return page_faults, page_hits, hit_ratio, miss_ratio

pages = [7, 0, 1, 2, 0, 3, 0,
             4, 2, 3, 0, 3, 2]
n = len(pages)
capacity = 4
# page_faults, page_hits, hit_ratio, miss_ratio = FIFO(pages, n, capacity)
# page_faults, page_hits, hit_ratio, miss_ratio = LRU(pages, n, capacity)
page_faults, page_hits, hit_ratio, miss_ratio = MRU(pages, n, capacity)
# page_faults, page_hits, hit_ratio, miss_ratio = OptimalPage(pages, n, capacity)

print("Page Faults:", page_faults)
print("Page Hits:", page_hits)
print("Hit Ratio:", hit_ratio)
print("Miss Ratio:", miss_ratio)
