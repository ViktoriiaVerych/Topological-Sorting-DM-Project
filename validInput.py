def isValid(prompt, validFunc, errorMessage):
    # Check if user's prompt/input is correct
    # using memoization to save previous valid inputs
    memo = {}
    while True:
        userInput = input(prompt)
        if userInput in memo:
            isValid = memo[userInput]
        else:
            isValid = validFunc(userInput)
            memo[userInput] = isValid
        if isValid:
            return userInput
        print(errorMessage)


def isNonZeroPositive(s):
    # Check if nonzero positive value
    return s.isdigit() and int(s) > 0


def floatValid(s):
    # Check if value is between 0 and 1
    if s.count('.') > 1:
        return False
    if s == '.':
        return False
    return all(char.isdigit() or char == '.' for char in s) and 0 < float(s) <= 1
