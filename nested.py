# Author "Chris Wilson, Sean, Janell, Koren, Kano"

import sys


def is_matched(s):
    brac_types = {
        "parasts": ["(*", "*)"],
        "parens": ["(", ")"],
        "squares": ["[", "]"],
        "curlies": ["{", "}"],
        "alligators": ["<", ">"]
    }

    opn_bracket = []
    index = 0
    answer = "Yes"
    while s:
        index += 1
        if s[:2] == "(*" or s[:2] == "*)":
            token = s[:2]
        else:
            token = s[0]
        for bracket_maybe in brac_types:
            if token == brac_types[bracket_maybe][0]:
                opn_bracket.append(token)
            if token == brac_types[bracket_maybe][-1]:
                if opn_bracket[-1] != brac_types[bracket_maybe][0]:
                    answer = "NO " + str(index)
                    token = s
                else:
                    opn_bracket.pop()
        s = s[len(token):]
    if len(opn_bracket) > 0:
        answer = "NO " + str(index)
    return answer


def is_nested(line):
    """Validate a single input line for correct nesting"""
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # linecount = 0
    answer = ''
    with open('input.txt', 'r') as rf:
        for s in rf:
            answer += is_matched(s) + '\n'
            # linecount += 1
    with open('output.txt', 'w') as wf:
        wf.write(answer)


if __name__ == '__main__':
    main('input.txt')
