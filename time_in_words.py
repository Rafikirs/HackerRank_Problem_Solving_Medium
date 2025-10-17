# Exercise: The Time in Words
# URL: https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
# Description: Convert a numeral time into words

def number_to_words(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty"]

    if n < 20:
        return ones[n]
    elif n < 60:
        ten, one = divmod(n, 10)
        return tens[ten] if one == 0 else f"{tens[ten]} {ones[one]}"
    else:
        return str(n)


def timeInWords(h, m):
    if m == 0:
        return f"{number_to_words(h)} o' clock"
    elif m == 15:
        return f"quarter past {number_to_words(h)}"
    elif m == 30:
        return f"half past {number_to_words(h)}"
    elif m == 45:
        next_hour = h + 1 if h < 12 else 1
        return f"quarter to {number_to_words(next_hour)}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{number_to_words(m)} {minute_word} past {number_to_words(h)}"
    else:
        remaining = 60 - m
        next_hour = h + 1 if h < 12 else 1
        minute_word = "minute" if remaining == 1 else "minutes"
        return f"{number_to_words(remaining)} {minute_word} to {number_to_words(next_hour)}"
