from typing import List, Tuple

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    result: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), letters, numbers))
    print(result)
