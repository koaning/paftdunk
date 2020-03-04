def window(seq):
    for idx in range(len(seq) - 1):
        yield seq[idx], seq[idx+1]
        yield seq[idx + 1], seq[idx]
