from statement_crunch.credit_statement import AbstractStatement
from statement_crunch.entry import Entry


class BmoStatement(AbstractStatement):
    @staticmethod
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

        return Entry(
            day=int(words[3]),
            month=words[2].removesuffix("."),
            year=year,
            description=description,
            dollar_amount=dollar_amount,
            credit=credit,
        )
