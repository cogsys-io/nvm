#!/usr/bin/env python3

import os
import pwd
import socket
import pathlib
import logging


from typing import (
    Dict,
    Optional,
)


def chdir(
    locations: Dict[str, Dict[str, str]],
    log0: Optional[logging.Logger] = logging.getLogger("dummy"),
) -> str:
    """Change current directory according to hostname and username.

    Target directory path is relative to user's ``${HOME}`` directory.

    Parameters
    ----------
    locations : Dict[str, Dict[str, str]]
        Dictionary containing locations, usernames and paths.
    log0 : Optional[logging.Logger]
        Logger.

    Examples
    --------
    >>> import srsly
    >>> import nvm
    >>> locations = \'\'\'
    >>> stardust7:
    >>>   jiko: cc/dev/
    >>> buka2:
    >>>   jiko: cc/cfg/
    >>> \'\'\'
    >>> locations = srsly.yaml_loads(locations)
    >>> print(nvm.chdir(locations))

    """
    hostname = str(socket.gethostname())
    username = str(pwd.getpwuid(os.getuid()).pw_name)
    log0.debug(f"{hostname = }")
    log0.debug(f"{username = }")
    # TODO: add warning if mach is found for hostname or username
    if hostname in locations.keys():
        if username in locations[hostname].keys():
            os.chdir(pathlib.Path.home() / locations[hostname][username])
            log0.info(f"{os.getcwd() = }")

    return pathlib.Path.cwd()
