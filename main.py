import pandas as pd
import argparse
from typing import List
from typing import Dict


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()


def get_year_stats(table: List[List[object]]) -> Dict:
    years_count = {}
    for i in table:
        if i[1] in years_count:
            years_count[i[1]] += 1
        else:
            years_count[i[1]] = 1
    return years_count


def get_most_mentioned_artist(table: List[List[object]]) -> str:
    most_popular = {}
    for i in table:
        if i[7] in most_popular:
            most_popular[i[7]] += 1
        else:
            most_popular[i[7]] = 1
    most_mentioned_artist = max(most_popular, key=most_popular.get)
    return most_mentioned_artist


def some_func(n):
    print('Принял численный аргумент ', n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="our cute spotify experience")
    parser.add_argument("file_path", type=str, help="input path to the table")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-n", "--number", action="store_true")
    args = parser.parse_args()
    table = open_file(args.file_path)
    if args.verbose:
        print("Most popular year:", max(get_year_stats(table)))
    if args.number:
        print("Most popular artist:", get_most_mentioned_artist(table))

