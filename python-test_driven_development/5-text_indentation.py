#!/usr/bin/python3
"""
Module: 5-text_indentation

Prints a text with 2 new lines after each of these characters: . ? :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after specific characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        idx = 0
        for char in text:
            if idx == 0:
                if char == " ":
                    continue
                else:
                    idx = 1
            if idx == 1:
                if char in ['.', '?', ':']:
                    print(char + '\n')
                    idx = 0
                else:
                    print(char, end="")
