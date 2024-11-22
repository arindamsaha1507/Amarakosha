"""Create data for the project."""

import json
import pathlib


def read_json(file_path: pathlib.Path) -> dict:
    """Read a JSON file and return the data as a dictionary."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def collect_words(data: dict, filename: pathlib.Path) -> None:
    """Collect all the words from the data."""

    content: list[dict] = data["data"]

    with open(filename, "w", encoding="utf-8") as file:
        for item in content:
            words = item["words"]
            num = item["num"]
            for word in words:
                linga = word["linga"]
                file.write(f"{word["word"]},{linga},{num}\n")


def collect_shlokas(data: dict, filename: pathlib.Path) -> None:
    """Collect all the shlokas from the data."""

    content: list[dict] = data["data"]

    with open(filename, "w", encoding="utf-8") as file:
        for item in content:
            shloka = item["text"]
            num = item["num"]
            file.write(f"{shloka},{num}\n")


def collect_synonyms(data: dict, filename: pathlib.Path) -> None:
    """Collect all the synonyms from the data."""

    content: list[dict] = data["data"]

    with open(filename, "w", encoding="utf-8") as file:
        for item in content:
            words = item["words"]
            for word in words:
                synonyms = " ".join(word["synonyms"])
                file.write(f"{word["word"]},{word["artha"]},{synonyms}\n")


def main() -> None:
    """Create the data for the project"""

    data_path = pathlib.Path("amara.json")
    data = read_json(data_path)

    words_path = pathlib.Path("words.csv")
    collect_words(data, words_path)

    shlokas_path = pathlib.Path("shlokas.csv")
    collect_shlokas(data, shlokas_path)

    synonyms_path = pathlib.Path("synonyms.csv")
    collect_synonyms(data, synonyms_path)


if __name__ == "__main__":
    main()
