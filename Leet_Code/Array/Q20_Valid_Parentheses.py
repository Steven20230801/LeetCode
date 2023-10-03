# Valid Parentheses

s1 = "()[]{}"
s2 = "([)]"
s3 = "{[]}"
s4 = "){"


def isValid(s):
    # using hash table
    stack = []
    table = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char not in table:  # if char is not in table, it is a left bracket
            stack.append(char)  # append left bracket to stack
        elif (
            not stack or table[char] != stack.pop()
        ):  # if stack is empty or char is not the corresponding right bracket
            return False
    return len(stack) == 0


print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
