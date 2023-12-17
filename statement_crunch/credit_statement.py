import dataclasses
from typing import List, Optional
from pypdf import PdfReader
import re


MONTHS = ["Jan", "Fev", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

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

@dataclasses.dataclass()
class Entry:
    """Note: year and date (month and day) have been separated
    """
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    process_date: Optional[str] = None
    description: Optional[str] = None
    dollar_amount: Optional[str] = None
    credit: Optional[bool] = None

    def __str__(self) -> str:
        return f"{self.month}/{self.year}/{self.day}, {self.description}, ${self.dollar_amount}"

def categorize(payment_line: str, year: str = None) -> Entry:
    words = payment_line.split()
    credit = False
    dollar_amount = words[-1]
    if dollar_amount == "CR":
        credit = True
        dollar_amount = words[-2]


    description_words = words[4:-3]

    description = ""
    for i in range(len(description_words)):
        description += description_words[i]
        if i != len(description_words) - 1:
            description += " "
    
    return Entry(day=None, month=None, year=year, process_date=f"{words[2]} {words[3]}", description=description, dollar_amount=dollar_amount, credit=credit)

def get_year(first_page) -> int:
    """Gets date from first page. Note: Entries extracted do not contain the year so this function is necessary

    Returns:
        Year found
    """
    match = re.search(r"[0-9][0-9], [0-9][0-9][0-9][0-9]", first_page.extract_text())
    year = re.search(r"[0-9][0-9][0-9][0-9]", match.group(0))
   
    return int(year.group(0))
def bmo_statement_pull_payments(pdf) -> List[Entry]:
    result = []
    reader = PdfReader(pdf)
    year = get_year(reader.pages[0])
    for page in reader.pages:
        for line in str(page.extract_text()).splitlines():
            if starts_w_month(line) and len(line) > DATE_LINE_LEN:
                result.append(categorize(line, year))

    return result

def save_csv(entries: List[Entry], path:str = None):
    """Saves entries to a csv file.

    Args:
        entries (List[Entry]): _description_
        path (str, optional): _description_. Defaults to None.
    """
    pass

for entry in bmo_statement_pull_payments("statements/December 21, 2021.pdf"):
    print(entry)
