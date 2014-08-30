d1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
d2 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "nineteen", "twenty"]
d3 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def convert(n):
    if n <= 10:
        return d1[n - 1]
    elif 11 <= n <= 20:
        return d2[n - 11]
    elif 21 <= n < 100:
        if n % 10 != 0:
            return d3[n // 10 - 1] + "-" + d1[n % 10 - 1]
        else:
            return d3[n // 10 - 1]
    elif 100 <= n <= 1000:
        if n % 100 == 0:
            return d1[n // 100 - 1] + " hundred"
        elif n % 10 == 0:
            return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1]
        else:
            if 11 <= n % 100 <= 20:
                return d1[n // 100 - 1] + " hundred and " + d2[n%100 - 11]
            elif 21 <= n % 100 < 100:
                if n % 100 % 10 != 0:
                    return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1] + "-" + d1[n % 100 % 10 - 1]
                else:
                    return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1]

print(convert(5))
print(convert(15))
print(convert(50))
print(convert(99))
print(convert(210))
print(convert(350))
print(convert(315))
print(convert(355))