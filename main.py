#! /usr/bin/env python3
    
def main():
    text = input()
    convert(text)

def convert(text):
    g = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    e = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    gl = g.lower()
    el = e.lower()

    english_to_greek = {
        "A": "Α",
        "B": "Β",
        "E": "Ε",
        "Z": "Ζ",
        "H": "Η",
        "I": "Ι",
        "K": "Κ",
        "M": "Μ",
        "N": "Ν",
        "O": "Ο",
        "P": "Ρ",
        "T": "Τ",
        "Y": "Υ",
        "X": "Χ",
    }

    print(text.translate(str.maketrans(english_to_greek)).lower())

if __name__ == "__main__":
    main()
