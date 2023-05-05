#!/usr/bin/env python3

import re
import pytest  # noqa: F401
from nvm import nvm  # noqa: F401

from nvm.aux_str import clean_str
from nvm.aux_str import CLEAN_STR_MAPPINGS_TINY


class TestAuxStr:
    def test_clean_str_one(self):
        text_dirty = "  one two  three\t \n\n\r four...  "
        text_clean = clean_str(text=text_dirty, mappings=CLEAN_STR_MAPPINGS_TINY)
        assert text_clean == "one two three four..."

    def test_clean_str_zero(self):
        mappings = [{"": [re.compile(r".*")]}]
        text_dirty = "abcABC"
        text_clean = clean_str(text=text_dirty, mappings=mappings)
        assert text_clean == ""

    def test_clean_str_re(self):
        mappings = [{"": [re.compile(r"[abc]")]}]
        text_dirty = "abcABC"
        text_clean = clean_str(text=text_dirty, mappings=mappings)
        assert text_clean == "ABC"

    def test_clean_str_rei(self):
        mappings = [{"": [re.compile(r"[abc]", re.I)]}]
        text_dirty = "abcABC"
        text_clean = clean_str(text=text_dirty, mappings=mappings)
        assert text_clean == ""

    def test_clean_str_non_awkward_mappings(self):
        mappings = [{"a": list("ABC")}, {"e": list("EFG")}]
        text_dirty = "ABCEFG"
        text_clean = clean_str(text=text_dirty, mappings=mappings)
        assert text_clean == "aaaeee"

    def test_clean_str_awkward_mappings(self):
        mappings = [{"a": list("ABC"), "e": list("EFG")}]
        text_dirty = "ABCEFG"
        text_clean = clean_str(text=text_dirty, mappings=mappings)
        assert text_clean == "aaaeee"
