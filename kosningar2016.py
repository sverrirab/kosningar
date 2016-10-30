import itertools

MAJORITY = 32  # out of 63

RESULTS = {'A': 4, 'C': 7, 'B': 8, 'D': 21, 'P': 10, 'S': 3, 'V': 10}
ALL = "".join(sorted(RESULTS.keys()))


def normalize(t):
    """
    Get a sorted list of party letters for inserting into set/hash.
    :param t: set of letters
    :return: string with sorted letters
    """
    return "".join(sorted(list(t)))


def count_majority(possibility):
    """
    Count number of MP's for given possibility.
    :param possibility: string in normalized form
    :return: number of MP's
    """
    total = 0
    for party in possibility:
        total += RESULTS[party]
    return total


def get_possibilities(num):
    """
    Get all possible combinations of 'num' parties that have majority.
    :return: num_checked, possibilities
    """
    count = 0
    possible = set()
    for p in itertools.combinations(RESULTS, num):
        count += 1
        if count_majority(p) >= MAJORITY:
            possible.add(normalize(p))

    return count, possible


def seen_one_less(unique, possibility):
    """
    Run all combinations of parties with one removed we have already seen.
    :param unique: All working combinations seen
    :param possibility: The new combination to check (in normalized form)
    :return: True if this 'possibility' has been seen with one party removed
    """
    all_lesser = []
    for i in range(1, len(possibility)):
        all_lesser.extend([x for x in itertools.combinations(possibility, i)])
    #print possibility, "all_lesser:", all_lesser

    for a in all_lesser:
        if normalize(a) in unique:
            #print "found one:", normalize(a)
            return True
    return False



def all_possibilities():
    """
    Get all possible combinations of parties that can create a majority.
    :return: set of possibilities.
    """
    unique = set()
    checked = set()
    for num in range(1, len(RESULTS)):
        count, possibilities = get_possibilities(num)
        # Remove options already in the list with one party removed.
        new = set()
        for possibility in possibilities:
            if not seen_one_less(unique, possibility) or possibility in checked:
                new.add(possibility)
                unique.add(possibility)
        if len(new) > 0:
            print "With", num, "parties - ", len(possibilities), "out of", count, "have majority"
            print "Of those there are", len(new), "new options:"
            for n in new:
                matrix = []
                for p in ALL:
                    if p in n:
                        matrix.append(p)
                    else:
                        matrix.append("")
                matrix.append(str(count_majority(n)))
                matrix.append(str(num))
                print ", ".join(matrix)

            print ""


def main():
    all_possibilities()


if __name__ == "__main__":
    main()

