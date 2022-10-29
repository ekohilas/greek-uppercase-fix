#! /usr/bin/env python3
    
def main():
    text = input()
    converted_text = convert(text)
    print(converted_text)

def convert(text):

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

    return (
        text.translate(
            str.maketrans(english_to_greek)
        ).lower()
    )

if __name__ == "__main__":
    main()
