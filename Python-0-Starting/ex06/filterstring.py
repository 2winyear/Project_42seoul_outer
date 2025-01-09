import sys
from ft_filter import ft_filter


def main():
    """
    [main]

    This program that accepts two arguments: a string(S), and an integer(N). 
    The program should output a list of words from S that have 
    a length greater than N.
    """
    assert_string = "AssertionError: the arguments are bad"
    try:
        assert len(sys.argv) == 3, assert_string
    except AssertionError as e:
        print(e)
        sys.exit(1)


    is_val_int = True
    try:
        val = int(sys.argv[2])
    except ValueError:
        is_val_int = False
    
    try:
        assert is_val_int, assert_string
    except AssertionError as e:
        print(e)
        sys.exit(1)
    ft_list = sys.argv[1].split(' ')
    filtered_list = ft_filter(lambda x: len(x) > val, ft_list)
    print(f'{list(filtered_list)}')
    # print(f'origin list : [{ft_list}]')
    # print(f'filtered list : [{list(filtered_list)}]')

if __name__ == "__main__":
    main()
