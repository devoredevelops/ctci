def revStr(s):
    return s[::-1]

if __name__ == '__main__':
    words = ('mary', 'anna', 'peter')
    for w in words:
        print(f'revStr({w}): {revStr(w)}')
