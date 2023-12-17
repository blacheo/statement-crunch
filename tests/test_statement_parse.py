from pypdf import PdfReader
import pytest

from statement_crunch.credit_statement import get_year


STATEMENT_PATHS = ["statements/December 21, 2021.pdf", "statements/November 21, 2023.pdf"]

@pytest.mark.parametrize("pdf, expected_date", zip(STATEMENT_PATHS, [2021, 2023]))
def test_get_year(pdf, expected_date):
    reader = PdfReader(pdf)

    assert get_year(reader.pages[0]) == expected_date

