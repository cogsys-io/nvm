#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Top-level package for NVM."""

# fmt: off
from . import _version
__version__ = _version.get_versions()['version']
__version_dict__ = _version.get_versions()
# fmt: on

__author__ = """cogsys.io"""
__email__ = "cogsys@cogsys.io"


from .aux_sys import chdir
from .aux_str import clean_str
from .aux_log import Log0
from .aux_pandas import disp_df


def get_module_version():
    return __version__


# end
