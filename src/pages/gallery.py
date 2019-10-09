"""Gallery page used to navigate between examples"""
# IMPORTANT NOTES
# - For now modules from pages have to be reloaded every time we use them
# In order for this to work they should be added to the pages.__init__ file
# pylint: disable=invalid-name
import importlib

import streamlit as st

from . import spreadsheet

PAGES = {"Spreadsheet": spreadsheet, "Spreadsheet 2": spreadsheet}


def write():
    st.write(
        f"# Awesome Streamlit Gallery"
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
    if len(PAGES) > 1:
        selection = st.selectbox("Select App", list(PAGES.keys()))
    else:
        selection = list(PAGES.keys())[0]
    page = PAGES[selection]

    importlib.reload(page)  # Hack? To enable how reloading
    page.write()