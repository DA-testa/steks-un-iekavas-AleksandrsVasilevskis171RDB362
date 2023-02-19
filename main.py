# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
            pass

        if next in ")]}":
           
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0 or are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char,next)==False:
                return i+1
            opening_brackets_stack.pop()
            pass
    return len(opening_brackets_stack)  


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch ==0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
