#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    lines = []
    line_start = 0
    for i in range(len(text)):
        if text[i] in special_chars:
            lines.append(text[line_start:i+1].strip())
            line_start = i + 1
    lines.append(text[line_start:].strip())

    for line in lines:
        print(line)
