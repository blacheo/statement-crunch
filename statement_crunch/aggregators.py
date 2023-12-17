from typing import Dict, List

from statement_crunch.credit_statement import Entry




def monthly_sum_aggregator(entries: List[Entry]) -> dict[(int, int): int]:
    month_and_sum = dict()
    for entry in entries:
        if month_and_sum.get((entry.month, entry.year)) is not None:
            month_and_sum[(entry.month, entry.year)] += entry.credit
        else:
            month_and_sum[(entry.month, entry.year)] = entry.credit
    return month_and_sum