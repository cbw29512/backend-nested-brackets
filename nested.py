import sys
def is_matched(s):
    opn_bracket = []
    index = 0
    for chars in s:
        index += 1
        if s[index-1] + s[index] == "(*":
            opn_bracket.append(s[index-1] + s[index])
        if s[index-1] + s[index] == "*)":
            if len(opn_bracket) == 0:
                return 'No ' + str(index)
            if opn_bracket[-1] == "(*":
                opn_bracket.pop()
            else:
                return 'No ' + str(index)
        if chars == "(" or chars == "{" or chars == "<" or chars == "[":
            opn_bracket.append(chars)
        if chars == ")" or chars == "}" or chars == ">" or chars == "]":
            if len(opn_bracket) == 0:
                return 'No ' + str(index)
        if chars == ")":
            if opn_bracket[-1] == "(":
                opn_bracket.pop()
            else:
                return 'No ' + str(index)
        if chars == "}":
            if opn_bracket[-1] == "{":
                opn_bracket.pop()
            else:
                return 'No ' + str(index)
        if chars == ">":
            if opn_bracket[-1] == "<":
                opn_bracket.pop()
            else:
                return 'No ' + str(index)
        if chars == "]":
            if opn_bracket[-1] == "[":
                opn_bracket.pop()
            else:
                return 'No ' + str(index)
    if len(opn_bracket) == 0:
        return 'Yes'
    else:
        return 'No ' + str(index)
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
    main(sys.argv[1:])