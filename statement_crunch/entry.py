import dataclasses
from typing import Optional


@dataclasses.dataclass()
class Entry:
    """Note: year and date (month and day) have been separated"""

    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    process_date: Optional[str] = None
    description: Optional[str] = None
    dollar_amount: Optional[str] = None
    credit: Optional[bool] = None
    category: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.month}/{self.year}/{self.day}, {self.description}, ${self.dollar_amount}"
    
    def predict_category(self):
        raise NotImplementedError
    

