
def isValidNumber(s):
    return not (s.startswith('0') and len(s) > 1)

def add_str_nums(a, b):
    return str(int(a) + int(b))

def check_sum_string(s, start, len1, len2):
    num1 = s[start:start + len1]
    num2 = s[start + len1:start + len1 + len2]

    if not isValidNumber(num1) or not isValidNumber(num2):
        return False

    while start + len1 + len2 < len(s):
        sum_str = add_str_nums(num1, num2)
        sum_len = len(sum_str)

        next_start = start + len1 + len2
        next_end = next_start + sum_len

        if next_end > len(s) or s[next_start:next_end] != sum_str:
            return False

        num1, num2 = num2, sum_str
        start = start + len1
        len1, len2 = len2, sum_len

    return True

def isSumString(s):
    n = len(s)
    for len1 in range(1, n):
        for len2 in range(1, n - len1):
            if check_sum_string(s, 0, len1, len2):
                return True
    return False


print(isSumString("12243660"))     # True
print(isSumString("1111112223"))   # True
print(isSumString("123456"))       # False
print(isSumString("000"))          # True, because "0+0=0"
print(isSumString("0123"))         # False, leading zero invalid
