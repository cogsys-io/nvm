#!/usr/bin/env python3

import pathlib
import logging
from typing import (
    Dict,
    Union,
    Optional,
)


fn0_samp = (
    "../../data/"
    "data-001/sub-sykamw18_ses-evening_"
    "run-r0_date-20220725T202601."
    "uuid-670f238a-1c15-4f7c-be1a-ea057756ac04.csv"
)  # WTF


fn0 = (
    "../../data/"
    "data-001/sub-s001__ses-morning_"
    "insert_task-rest_space-T1w_desc-preproc_bold_info"
    ".the.funky_ext.nii.gz"
)


def dict_from_bids_filename(
    fn0: Union[str, pathlib.Path],
    log0: Optional[logging.Logger] = logging.getLogger("dummy"),
) -> Dict:
    """Extract tags, values, suffix(es) and extension(s) from BIDS-like filename.

    Parameters
    ----------

    fn0 : Union[str, pathlib.Path]
        BIDS-like filename (or path to such a file).

    Examples
    --------

    >>> from nvm.aux_bids import dict_from_bids_filename
    >>>
    >>> fn0_samp = (
    >>>     "../../data/"
    >>>     "data-001/sub-sykamw18_ses-evening_"
    >>>     "run-r0_date-20220725T202601."
    >>>     "uuid-670f238a-1c15-4f7c-be1a-ea057756ac04.csv"
    >>> )  # WTF
    >>>
    >>> fn0_samp = (
    >>>     "../../data/"
    >>>     "data-001/sub-s001__ses-morning_"
    >>>     "insert_task-rest_space-T1w_desc-preproc_bold_info"
    >>>     ".the.funky_ext.nii.gz"
    >>> )
    >>>
    >>> dict0 = dict_from_bids_filename(fn0_samp)
    >>> dict0
    {'props': {'sub': 's001',
      'ses': 'morning',
      'task': 'rest',
      'space': 'T1w',
      'desc': 'preproc'},
     'suff': ['insert', 'bold', 'info'],
     'ext': '.the.funky_ext.nii.gz'}


    >>> # Same example with added nice formatting
    >>> from nvm.aux_bids import dict_from_bids_filename
    >>> from nvm import jsonable
    >>> import srsly
    >>> import textwrap
    >>>
    >>> fn0_samp = (
    >>>     "../../data/"
    >>>     "data-001/sub-sykamw18_ses-evening_"
    >>>     "run-r0_date-20220725T202601."
    >>>     "uuid-670f238a-1c15-4f7c-be1a-ea057756ac04.csv"
    >>> )  # WTF
    >>>
    >>> fn0_samp = (
    >>>     "../../data/"
    >>>     "data-001/sub-s001__ses-morning_"
    >>>     "insert_task-rest_space-T1w_desc-preproc_bold_info"
    >>>     ".the.funky_ext.nii.gz"
    >>> )
    >>>
    >>> dict0 = dict_from_bids_filename(fn0_samp)
    >>>
    >>> print(
    >>>     "got:\\n" \\
    >>>     f"{textwrap.indent(srsly.yaml_dumps(jsonable(dict0)), 5*' ')}"
    >>> )
    got:
         props:
           sub: s001
           ses: morning
           task: rest
           space: T1w
           desc: preproc
         suff:
           - insert
           - bold
           - info
         ext: .the.funky_ext.nii.gz

    """
    fn0 = pathlib.Path(fn0)
    log0.debug(f"{fn0 = }")
    path0 = fn0.parent
    log0.debug(f"{path0 = }")
    name0 = fn0.name
    log0.debug(f"{name0 = }")
    ext = "".join(fn0.suffixes)
    log0.debug(f"{ext = }")
    # stem0 = fn0.stem             # NOTE: this fails for complex extensions
    # stem0 = fn0.with_suffix("")  # NOTE: (e.g., for ".tar.gz")
    # stem0 = fn0.name.rstrip("".join(fn0.suffixes))  # WTF
    # stem0 = name0.rstrip(ext)  # WTF
    stem0 = name0.split(".")[0]
    log0.debug(f"{stem0 = }")
    parts = [item for item in stem0.split("_") if len(item)]
    log0.debug(f"{parts = }")
    props = {item.split("-")[0]: item.split("-")[1] for item in parts if "-" in item}
    log0.debug(f"{props = }")
    suff = [item for item in parts if "-" not in item]
    log0.debug(f"{suff = }")
    tags0 = list(props.keys())
    log0.debug(f"{tags0 = }")
    vals0 = list(props.values())
    log0.debug(f"{vals0 = }")
    return dict(props=props, suff=suff, ext=ext)
