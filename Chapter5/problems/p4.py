def cichelli(wordlist):
    g = {}
    hashes = []

    for word in wordlist:
        g[word[0]] = 0
        g[word[-1]] = 0

    for word in wordlist:
        
        while True:
            h = len(word) + g[word[0]] + g[word[-1]]

            if h not in hashes:
                hashes.append(h)
                break
            g[word[0]] += 1
    
    return g, hashes

wordlist = ["advay","nidhi","harsh","apurv"]
g, hashes = cichelli(wordlist)
print(g)
print(hashes)