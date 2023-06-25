#!/usr/bin/env python3

import datetime as dt
import pytz
from pytz import timezone as tz

from typing import Union


def now(
    tz0: Union[str, pytz.BaseTzInfo] = "Europe/Berlin",
    fm0: str = "%Y%m%dT%H%M%S",
):
    """Get date and time as string (e.g., "20230201T070809").

    Parameters
    ----------
    tz0 : Union[str, pytz.BaseTzInfo]
        Timezone (defaults to "Europe/Berlin").
    fm0 : str
        Output string format (defaults to "%Y%m%dT%H%M%S").

    Returns
    -------
    str
        Date and time as string (e.g., "20230201T070809").

    Examples
    --------
    >>> from nvm import now
    >>> now()
    "20220607T024010"

    """

    if isinstance(tz0, pytz.BaseTzInfo):
        pass
    elif isinstance(tz0, str):
        tz0 = pytz.timezone(tz0)
    else:
        raise TypeError(
            f"Unexpected type for timezone (tz0) argument (expecting str or pytz.BaseTzInfo)"
        )

    return dt.datetime.now(tz0).strftime(fm0)
