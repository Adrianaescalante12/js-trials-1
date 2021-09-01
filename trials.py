"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print items from a list"""

    for item in items:
        print(item)
        

def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers."""
    
    even_nums  = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    """Given an array, return all elements at odd numbered indices."""

    return items[1::2]


def print_as_numbered_list(items):
    """Given an array, output a numbered list."""
    
    i = 0
    for item in items:
        print(f"{i}. {item}")
        i += 1
        

def get_range(start, stop):
    """Return an array of numbers in a certain range."""

    num_in_range = []
    while start < stop:
        num_in_range.append(start)
        start += 1

    return num_in_range

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'."""
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case."""

    camel_list = []
    words = string.split("_")
    camel_list = camel_list.append(words[0])
    del words[0]

    for word in words:
        camel_list.append(word[0].title())
    
    return ''.join(camel_list)

    #print(f"{words[0]}{words[1:][0].title()}")
    
    #    i = 1
    # for word in words:
    #     word[]

    # for i in range(len(string)):
    #     if string[i] != "_":
    #         camel_list.append(string[i])
    #         i += 1
    #     else:
    #         camel_list.append(string[i+1].upper())
    #         i += 2
    
    # return ''.join(camel_list)
        

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
