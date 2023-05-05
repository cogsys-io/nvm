#!/usr/bin/env python3


import re
from typing import (
    List,
    Dict,
)

from .clean_str_mappings import (  # noqa: F401
    CLEAN_STR_MAPPINGS_TINY,
    CLEAN_STR_MAPPINGS_LARGE,
    CLEAN_STR_MAPPINGS_HUGE,
)


def clean_str(
    text: str,
    mappings: List[Dict[str, List[str]]] = CLEAN_STR_MAPPINGS_TINY,
) -> str:
    """Clean string replacing any unwanted text with the desired.

    This function can be used to clean text from redundant whitespace characters
    and other common problems.

    Parameters
    ----------
    text : str
        Text to be cleaned.
    mappings : List[Dict[str, List[str]]]
        List of mappings to be used for text cleaning.
        This should be a list of dictionaries.
        Dictionary keys should contain strings that are
        used as replacement for matches of patterns provided
        as list in dictionary key value.

    Returns
    -------
    str
        Clean text.

    Examples
    --------

    To clean a string use:

    >>> from nvm.aux_str import clean_str
    >>> text_dirty = "  one two  three\\t \\n\\n\\r four...  "
    >>> text_clean = clean_str(text=text_dirty)
    >>> # print(text_dirty)
    >>> print(text_clean)
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
        for key, val in item.items():
            for pattern in val:
                text = re.sub(pattern, key, text)

    # Finally remove repeated whitespace characters
    text = re.sub(r"\s\s+", " ", text)
    # and strip whitespace at the beginning and end of the output
    text = text.strip()
    return text


def _temp_test_awkward_mappings():
    # mappings = [{"a": list("ABC")}, {"x": list("XYZ")}]
    mappings = [{"a": list("ABC"), "x": list("XYZ")}]
    for item in mappings:
        for key, val in item.items():
            for pattern in val:
                print(pattern, key)
