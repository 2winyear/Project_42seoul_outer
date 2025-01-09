import sys


def main():
    """
    [main]

    This program that takes a string as an argument and encodes it into Morse Code.
    """
    assert_string = "AssertionError: the arguments are bad"
    try:
        assert len(sys.argv) == 2, assert_string
        for c in sys.argv[1]:
            assert c.isalnum() or c == ' ', assert_string
    except AssertionError as e:
        print(e)
        sys.exit(1)
    NESTED_MORSE = {' ': '/',
                    'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    '0': '-----'
                    }
    morse_string = ''
    for c in sys.argv[1].upper():
        if morse_string == '':
            morse_string = NESTED_MORSE[c]
        else:
            morse_string = morse_string + ' ' + NESTED_MORSE[c]
    print(morse_string)


if __name__ == "__main__":
    main()