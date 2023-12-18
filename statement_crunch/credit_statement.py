from abc import ABC
import csv
from typing import List
from pypdf import PdfReader
import re

from statement_crunch.entry import Entry


MONTHS = [
    "Jan",
    "Fev",
    "Mar",
    "Apr",
    "Mai",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

MONTHS_TO_INT = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "Mai": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}

DATE_LINE_LEN = 29


def starts_w_month(line: str):
    if line[:3] in MONTHS:
        return True
    return False


class AbstractStatement(ABC):
    @staticmethod
    def get_year(first_page) -> int:
        """Gets date from first page. Note: Entries extracted do not contain the year so this function is necessary

        Returns:
            Year found
        """
        match = re.search(
            r"[0-9][0-9], [0-9][0-9][0-9][0-9]", first_page.extract_text()
        )
        year = re.search(r"[0-9][0-9][0-9][0-9]", match.group(0))

        return int(year.group(0))
    @staticmethod
    def categorize(line: str):
        raise NotImplementedError

    @staticmethod
    def is_entry_line(line: str) -> bool:
        return starts_w_month(line) and len(line) > DATE_LINE_LEN

    @classmethod
    def get_entries(cls, pdf) -> List[Entry]:
        reader = PdfReader(pdf)
        year = cls.get_year(reader.pages[0])

        lines = []
        for page in reader.pages:
            for line in page.extract_text().splitlines():
                lines.append(line)

        lines = filter(cls.is_entry_line, lines)

        return [cls.categorize(line, year) for line in lines]

    def save_csv(entries: List[Entry], path: str = None):
        """Saves entries to a csv file.

        Args:
            entries (List[Entry]): _description_
            path (str, optional): _description_. Defaults to None.
        """
        csv.writer()
        pass
