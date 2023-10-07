import pandas as pd
import argparse
from typing import List, Dict


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()


def get_year_stats(table: List[List[object]]) -> Dict:
    """
    returns
    {
        '2010': 123,
        '2011': 150,
        ....
        '2022': 300,
    }
    """
    return {}


def get_most_mentioned_artist(table: List[List[object]]) -> str:
    """
    returns
    the most mentioned artist in the dataset
    """
    return "artist_name"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path to the table")

    args = parser.parse_args()

    table = open_file(args.file_path)

    print(get_year_stats(table))
    print(get_year_stats(table))

python3 main.py playlist_2010to2022.csv