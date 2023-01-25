def allunique(s):
    charsTable = set()
    for c in s:
        if c in charsTable:
            return False
        charsTable.add(c)
    return True

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]

def allunique2(s):
    srtStr = sorted(s)
    return all(c1 != c2 for c1, c2 in pairs(srtStr))

if __name__ == '__main__':
    words = ('mary', 'ariadni')
    for w in words:
        print(f'allunique({w}): {allunique(w)}')
        print(f'allunique2({w}): {allunique2(w)}')
