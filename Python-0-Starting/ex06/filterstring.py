import sys
# ft_filter.py 파일이 같은 디렉토리에 있어야 합니다.
from ft_filter import ft_filter


def main():

    try:
        # 1. 인자 개수 확인 (스크립트명 제외 2개)
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        input_str = sys.argv[1]

        # 2. 숫자로만 된 문자열 거부 (필요 시)
        if input_str.isdigit():
            raise AssertionError("the arguments are bad")

        # 3. 두 번째 인자를 숫자로 변환
        try:
            i_number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # 4. 필터링 로직
        words = input_str.split()
        # lambda를 사용하여 길이가 input_number보다 큰 단어만 추출
        filtered_it = ft_filter(lambda word: len(word) > i_number, words)

        # 리스트 형태로 출력
        result = list(filtered_it)
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
