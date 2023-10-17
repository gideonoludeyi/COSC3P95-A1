import math


def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2
        else:
            output_str += char.upper()

    return output_str


def test(delta, expected, n=2):
    if processString(delta) == expected:
        return None  # this is a pass

    if len(delta) <= 1:
        return delta

    subsize = math.ceil(len(delta) / n)
    for i in range(0, len(delta), subsize):
        delta_i = delta[i:i+subsize]
        expdelta_i = expected[i:i+subsize]
        invdelta_i = delta[:i] + delta[i+subsize:]
        exp_invdelta_i = expected[:i] + expected[i+subsize:]
        if processString(delta_i) != expdelta_i:
            return test(delta_i, expdelta_i, 2) or delta
        elif processString(invdelta_i) != exp_invdelta_i:
            return test(invdelta_i, exp_invdelta_i, n-1) or delta
        else:
            return test(delta, expected, n*2) or delta


if __name__ == "__main__":
    test_cases = [
        ("abcdefG1", "ABCDEFg1"),
        ("CCDDEExy", "ccddeeXY"),
        ("1234567b", "1234567B"),
        ("8665", "8665"),
    ]
    for input_str, expected_str in test_cases:
        minimized_str = test(input_str, expected_str)
        print(minimized_str)
