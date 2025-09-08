from collections import Counter


def can_be_poly(string: str) -> bool:
    return len(list(filter(lambda x: x % 2 == 1, Counter(string).values()))) <= 1


if __name__ == "__main__":
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
