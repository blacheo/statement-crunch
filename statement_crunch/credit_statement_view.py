import streamlit as st
import numpy as np

from statement_crunch.credit_statement import bmo_statement_pull_payments




st.title("Credit Statement Cruncher")

pdfs = st.file_uploader("Upload Credit Card Statements Here", True)


if pdfs is not None:
    entries = []
    for pdf in pdfs:
        entries.extend(bmo_statement_pull_payments(pdf))
    
    monthly_sums = []
    np.bar()
