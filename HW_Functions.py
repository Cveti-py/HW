def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

print(calculate_area(10, 5))


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

print(is_even(4))
print(is_even(5))


def multiply_elements(numbers):
    """Multiply all elements in a list"""
    result = 1
    for number in numbers:
        result = result * number
    return result

print (multiply_elements ([2, 3, 4]))


def count_vowels(s):
    """Counts the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')

print(count_vowels("hello"))
print(count_vowels("world"))


def reverse_string(s):
    """Reverses a string"""
    return s[::-1]

print(reverse_string("hello"))


def remove_duplicates(items):
    """Removes duplicates from a list, preserving order"""
    return list(dict.fromkeys(items))

print(remove_duplicates([1, 2, 2, 3, 4, 3]))


def is_palindrome(word):
    """Check if a word is palindrome"""
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))


def lambda_add(x, y):
    """Returns the sum of two arguments"""
    return (lambda a, b: a+b)(x, y)

print(lambda_add(2, 3))


def filter_words(words, min_length):
    """Filters words by given minimum length"""
    return [word for word in words if len(word) > min_length]

print(filter_words(["apple", "pear", "banana", "cherry"], 5))


def sort_by_last_char(words):
    """Sorts words by their last character"""
    return sorted(words, key=lambda word: word[-1])

print(sort_by_last_char(["cherry", "banana", "apple"]))
