#!/usr/bin/env python3


CLEAN_STR_MAPPINGS_TINY = [
    {
        " ": [  # Unicode Character 'SPACE' (U+0020)
            "\n",  # LF (Line Feed)
            "\r",  # CR (Carriage Return)
            "\t",  # HT (Horizontal Tab)
        ],
    },
    {
        "-": [  # Unicode Character 'HYPHEN-MINUS' (U+002D) # chr(45) ord("-") ord("\u002D")
            "\u2212",  # Unicode Character 'MINUS SIGN' (U+2212)
            "\u2013",  # Unicode Character 'EN DASH' (U+2013) # chr(8211) ↔ ord("–") ↔ ord("\u2013")
            "\u2014",  # Unicode Character 'EM DASH' (U+2014)
            "\u2015",  # Unicode Character 'HORIZONTAL BAR' (U+2015)
            "\uFE63",  # Unicode Character 'SMALL HYPHEN-MINUS' (U+FE63)
            "\uFF0D",  # Unicode Character 'FULLWIDTH HYPHEN-MINUS' (U+FF0D)
        ],
    },
]

CLEAN_STR_MAPPINGS_LARGE = CLEAN_STR_MAPPINGS_TINY + [
    {
        " ": [  # Unicode Character 'SPACE' (U+0020)
            "\u200B",  # Unicode Character 'ZERO WIDTH SPACE' (U+200B)
            "\uFEFF",  # Unicode Character 'ZERO WIDTH NO-BREAK SPACE' (U+FEFF)
            "\u202F",  # Unicode Character 'NARROW NO-BREAK SPACE' (U+202F)
            "\u00A0",  # Unicode Character 'NO-BREAK SPACE' (U+00A0)
            "\u200E",  # Unicode Character 'LEFT-TO-RIGHT MARK' (U+200E)
            "\u3164",  # Unicode Character 'HANGUL FILLER' (U+3164).
            "\\&nbsp;",  # just in case a HTML leaked in
        ],
    },
    {
        "'": [  # Unicode Character 'APOSTROPHE' (U+0027)
            "’",
            "‘",
            "‛",
            "‚",
            "′",
        ],
    },
    {
        '"': [
            "“",
            "”",
            "„",
        ],
    },
]

CLEAN_STR_MAPPINGS_HUGE = CLEAN_STR_MAPPINGS_LARGE + []  # TODO
