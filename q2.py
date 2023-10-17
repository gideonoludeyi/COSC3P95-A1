import sys
import random


def sort(items):
    """an implementation of the insertion sort algorithm
    with a bug in the while loop
    """
    # create a copy of the list to sort in-lacep
    copy = list(items)

    for i in range(1, len(copy)):
        while i > 1 and copy[i-1] > copy[i]:
            copy[i], copy[i-1] = copy[i-1], copy[i]
            i -= 1

    return copy


def mutate(intlist):
    """generates mutations of the input integer list
    by apply the following transformations:
    1. Swap - for every unordered pair of elements, swap them so their order is corrected
    2. Extend - appends a random number of random integers to the input integer list
    """
    # the list of generated test cases where each element is a (input list, expected list) tuple
    mutated_test_cases = []

    # Swap - generates a new test case for every unordered pair
    #  by swapping the order of the unordered pair
    expected = sorted(intlist)
    for i in range(len(intlist)-1):
        if intlist[i] > intlist[i+1]:
            test_case = list(intlist)
            test_case[i], test_case[i+1] = test_case[i+1], test_case[i]
            mutated_test_cases.append((test_case, expected))

    # Extend - generates a random number of new test cases that append
    #  random integers to the original input
    for i in range(random.randint(1, 10)):
        appended_values = [
            random.randint(-100, 100)
            for _ in range(random.randint(1, 10))
        ]
        test_case = intlist + appended_values
        mutated_test_cases.append((test_case, sorted(test_case)))

    return mutated_test_cases


def randtest(n, test_cases):
    # exit the random test case generator when there's no more test case
    for _ in range(n):  # run the random test case generator up to n times
        if len(test_cases) == 0:
            return

        # pull out a random test case from the list of test cases
        inp, exp = random.choice(test_cases)
        test_cases.remove((inp, exp))

        try:
            out = sort(inp)  # run the algorithm on the random test case
        except Exception as e:  # report any exception that was encountered in the algorithm
            print(f"Fail: input was {inp}; but got exception `{e}`")
        else:
            if out != exp:
                print(f"Fail: input was {inp}; expected {exp}; but got {out}")
                # add mutations of the input to be tested later
                test_cases.extend(mutate(inp))
            else:
                print(f"Pass: input was {inp}; output was {out}")


if __name__ == "__main__":
    # determine how many times to run the random test case generator
    #  using CLI input
    #  default: 30
    n_runs = int(sys.argv[1]) if len(sys.argv) >= 2 else 30

    # the initial set of test cases: a list of (input list, expected list) tuples
    test_cases = [
        ([], []),
        ([7], [7]),
        ([-43, 23], [-43, 23]),
        ([23, -43], [-43, 23]),
    ]

    randtest(n_runs, test_cases)
