import sys


def counter(text):
    """
    [counter]
    This is count function
    """
    total = 0
    upper = 0
    lower = 0
    p_mark = 0
    space = 0
    digit = 0
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[]\\^_`{|}~'

    for i in text:
        total += 1
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in punctuation:
            p_mark += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
    print(f'The text contains {total} characters:')
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{p_mark} punctuation marks')
    print(f'{space} spaces')
    print(f'{digit} digits')


def main():
    """
    [main]
    This time you have to make a real autonomous program, with a main, which
    takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters,
    digits and spaces.
    """

    assert_string = "AssertionError: more than one argument is provided"

    try:
        assert len(sys.argv) < 3, assert_string
    except AssertionError as e:
        print(e)
        sys.exit(1)
    if len(sys.argv) == 1 or sys.argv[1] == '':
        try:
            print('What is the text to count?')
            input_text = sys.stdin.read()
            counter(input_text)
        except KeyboardInterrupt:
            sys.exit()
    else:
        counter(sys.argv[1])


if __name__ == "__main__":
    main()
