def compress(str_):

    if len(str_) < 2:
        return str_

    groups = []
    previous_character = str_[0]
    counter = 1

    for c in str_[1:]:
        if c == previous_character:
            counter += 1
        else:
            groups.append(previous_character + str(counter))
            previous_character = c
            counter = 1
    groups.append(c + str(counter))
    result = ''.join(groups)
    return result if len(result) < len(str_) else str_


import itertools

def compress(str_):
    """ Using itertools.groupby().

    There is a function in the standard library, itertools.groupby() (new in
    Python 2.4), that does exactly what we need here: it makes an iterator that
    returns consecutive keys and groups from the input iterable, defaulting to
    an identity function to compute the key value for each element. Example:

    >>> [list(g) for k, g in itertools.groupby('AAAABBBCCD')]
    [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]

    """

    groups = itertools.groupby(str_)
    compressed = ''.join('{0}{1}'.format(k, len(list(g))) for k, g in groups)
    return compressed if len(compressed) < len(str_) else str_

if __name__ == '__main__':
    words = ('aabcccccaaa', 'aaabbbbcccccdee', 'abc', 'a', '', ' ', 'aabccdde', 'aab', 'aaabb')
    for w in words:
        print(f'compress({w}): {compress(w)}')
