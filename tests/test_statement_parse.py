import os
from typing import List
from pypdf import PdfReader
import pytest
from statement_crunch.entry import save_csv

from statement_crunch.statement_types.bmo_statement import BmoStatement


STATEMENT_PATHS = ["statements/December 21, 2021.pdf", "statements/November 21, 2023.pdf"]

@pytest.mark.skipif(not os.path.exists("/statements"), reason="requires statements to exist")
@pytest.mark.parametrize("pdf, expected_date", zip(STATEMENT_PATHS, [2021, 2023]))
def test_get_year(pdf, expected_date):
    reader = PdfReader(pdf)

    assert BmoStatement.get_year(reader.pages[0]) == expected_date


def test_filter_for_entries():
    expected_entries = ["Dec. 2023, Oct. 2023, DOLLARAMA, #12312 .24", "Oct. 2023, Dec 2023, WALMART, #1234 3.23",]

    lines_to_test = ["Dec. 2023, Oct. 2023, DOLLARAMA, #12312 .24", "Oct. 2023, Dec 2023, WALMART, #1234 3.23", "hello_world", "Dec 2023,"]

    assert list(filter(BmoStatement.is_entry_line, lines_to_test)) == expected_entries

@pytest.mark.skipif(not os.path.exists("/statements"), reason="requires statements to exist")
@pytest.mark.parametrize("pdf_path, expected_entries", zip(STATEMENT_PATHS, [[], []]))
def test_get_entries(pdf_path, expected_entries):
    entries = BmoStatement.get_entries(pdf_path)
    assert entries == expected_entries

@pytest.mark.skipif(not os.path.exists("/statements"), reason="requires statements to exist")
@pytest.mark.parametrize("pdf_path", STATEMENT_PATHS)
def test_generate_csv(pdf_path):
    save_csv(BmoStatement.get_entries(pdf_path), f"output/{pdf_path}")