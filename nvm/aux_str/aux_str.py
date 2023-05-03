#!/usr/bin/env python3


import re
from typing import List, Dict


CLEAN_STR_MAPPINGS_TINY = [
    dict(
        new=" ",  # Unicode Character 'SPACE' (U+0020)
        old=[
            "\n",
            "\r",
            "\t",
        ],
    ),
    dict(
        new="-",  # Unicode Character 'HYPHEN-MINUS' (U+002D) # chr(45) ord("-") ord("\u002D")
        old=[
            "\u2212",  # Unicode Character 'MINUS SIGN' (U+2212)
            "\u2013",  # Unicode Character 'EN DASH' (U+2013) # chr(8211) ↔ ord("–") ↔ ord("\u2013")
            "\u2014",  # Unicode Character 'EM DASH' (U+2014)
            "\u2015",  # Unicode Character 'HORIZONTAL BAR' (U+2015)
            "\uFE63",  # Unicode Character 'SMALL HYPHEN-MINUS' (U+FE63)
            "\uFF0D",  # Unicode Character 'FULLWIDTH HYPHEN-MINUS' (U+FF0D)
        ],
    ),
]

CLEAN_STR_MAPPINGS_LARGE = [
    dict(
        new=" ",  # Unicode Character 'SPACE' (U+0020)
        old=[
            "\n",
            "\r",
            "\t",
            "\u200B",  # Unicode Character 'ZERO WIDTH SPACE' (U+200B)
            "\uFEFF",  # Unicode Character 'ZERO WIDTH NO-BREAK SPACE' (U+FEFF)
            "\u202F",  # Unicode Character 'NARROW NO-BREAK SPACE' (U+202F)
            "\u00A0",  # Unicode Character 'NO-BREAK SPACE' (U+00A0)
            "\u200E",  # Unicode Character 'LEFT-TO-RIGHT MARK' (U+200E)
            "\u3164",  # Unicode Character 'HANGUL FILLER' (U+3164).
            "\\&nbsp;",  # just in case a HTML leaked in
        ],
    ),
    dict(
        new="-",  # Unicode Character 'HYPHEN-MINUS' (U+002D) # chr(45) ord("-") ord("\u002D")
        old=[
            "\u2212",  # Unicode Character 'MINUS SIGN' (U+2212)
            "\u2013",  # Unicode Character 'EN DASH' (U+2013) # chr(8211) ↔ ord("–") ↔ ord("\u2013")
            "\u2014",  # Unicode Character 'EM DASH' (U+2014)
            "\u2015",  # Unicode Character 'HORIZONTAL BAR' (U+2015)
            "\uFE63",  # Unicode Character 'SMALL HYPHEN-MINUS' (U+FE63)
            "\uFF0D",  # Unicode Character 'FULLWIDTH HYPHEN-MINUS' (U+FF0D)
        ],
    ),
    dict(
        new="'",  # Unicode Character 'APOSTROPHE' (U+0027)
        old=[
            "’",
            "‘",
            "‛",
            "‚",
            "′",
        ],
    ),
    dict(
        new='"',
        old=[
            "“",
            "”",
            "„",
        ],
    ),
]


def clean_str(
    text: str, mappings: List[Dict[str, List[str]]] = CLEAN_STR_MAPPINGS_TINY
) -> str:
    """
    Clean string replacing any unwanted text with the desired.

    This function can be used to clean text from redundant whitespace characters
    and other common problems.

    Parameters
    ----------
    text : str
        Text to be cleaned.
    mappings : List[Dict[str, List[str]]]
        List of mappings to be used for text cleaning.
        TODO: This has been changed to a list of dictionaries,
        each containing two keys "new" and "old".
        The "new" is used to reference a string that will replace
        each of the strings in the list referenced by "old" key.

    Returns
    -------
    str
        Clean text.

    Examples
    --------

    To clean a string use:

    >>> from nvm.aux_str import clean_str
    >>> text_dirty = "  one  two\t  three  \t\t four...  "
    >>> clean_str(text=text_dirty)
    "one two three four..."

    This function comes handy with pandas dataframes:

    >>> # let df0 be a dataframe that contains text column "text"
    >>> # to clean its content in place we may run
    >>> text_field = "text"
    >>> df0[text_field] = df0[text_field].apply(clean_str)

    .. role:: python(code)
        :language: python
    
    The mappings argument should be a list of dictionaries with
    keys containing the desired replacement values containing
    a list of replaced items (:python:`List[Dict[str, List[str]]]`).

    >>> # Import example mappings
    >>> from nvm.aux_str import CLEAN_STR_MAPPINGS_TINY
    >>> from nvm.aux_str import CLEAN_STR_MAPPINGS_LARGE
    >>> # Display them as JSON:
    >>> import srsly
    >>> print(srsly.json_dumps(CLEAN_STR_MAPPINGS_TINY, indent=2))

    Note that we used |json_dumps|_ function from the |srsly|_ library
    to get indented JSON output.

    .. |srsly| replace:: ``srsly``
    .. _srsly: https://github.com/explosion/srsly

    .. |json_dumps| replace:: ``json_dumps``
    .. _json_dumps: https://github.com/explosion/srsly/blob/136eb677604e65fd4f00ce9594c6f558b1fc2d3c/srsly/_json_api.py#L10  ## noqa: E501

    """
    # make sure that the text input is str
    text = str(text)
    # substitute each undesired str with the desired one
    for item in mappings:
        for pattern in item["old"]:
            text = re.sub(pattern, item["new"], text)

    # Finally remove repeated whitespace characters
    text = re.sub(r"\s\s+", " ", text)
    # and strip whitespace at the beginning and end of the output
    text = text.strip()
    return text
