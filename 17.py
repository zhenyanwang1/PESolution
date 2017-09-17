import string

d1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
d2 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
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
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return d1[n // 100 - 1] + " hundred"
        elif n % 10 == 0:
            return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1]
        else:
            if 1 <= n % 100 <= 10:
                return d1[n // 100 - 1] + " hundred and " + d1[n % 100 - 1]
            elif 11 <= n % 100 <= 20:
                return d1[n // 100 - 1] + " hundred and " + d2[n % 100 - 11]
            elif 21 <= n % 100 < 100:
                if n % 100 % 10 != 0:
                    return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1] + "-" + d1[n % 100 % 10 - 1]
                else:
                    return d1[n // 100 - 1] + " hundred and " + d3[n % 100 // 10 - 1]
    elif n == 1000:
        return "one thousand"

print(convert(990))
snums = []
for i in range(1, 1000 + 1):
    snums.append(convert(i))
total = 0
for snum in snums:
    for chr in snum:
        if chr in string.ascii_lowercase:
            total += 1
print(total)