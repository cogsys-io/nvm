#!/usr/bin/env python3

import re

# "abc[-]xyz[*]"-like
REGEX_ABC_DASH_XYZ_ASTERISK = re.compile(r"^[a-z]+(\-[a-z]+)*\*?$", re.IGNORECASE)
