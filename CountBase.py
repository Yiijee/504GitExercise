def countBase(DNA):
    Counts = dict() # store the counts of each base 
    for base in DNA:
        if base not in Counts:
            Counts[base] = 1
        else:
            Counts[base] += 1
    return Counts

def baseFreq(Counts):
    print('freqs')
    total = float(sum([Counts[base] for base in Counts.keys()]))
    for base in Counts.keys():
        print(base + ':' + str(Counts[base]/total))
if __name__ == "__main__":
    baseFreq(countBase('ATCTGACGCGCGCCGC'))
