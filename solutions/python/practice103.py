# Calculate Percentage of Letter in String

def letter_percentage(s, c):
    if not s:
        return 0
    return int(s.lower().count(c.lower()) / len(s) * 100)


if __name__ == "__main__":
    s = input("Enter a string: ")
    c = input("Enter a character: ")
    print(f"Percentage: {letter_percentage(s, c)}%")


# Test cases with assertions
assert letter_percentage("hello", "l") == 40
assert letter_percentage("Hello", "H") == 20
assert letter_percentage("abc", "z") == 0
assert letter_percentage("aaaa", "A") == 100
assert letter_percentage("", "a") == 0

print("All test cases passed!")
