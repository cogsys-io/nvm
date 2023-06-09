#!/usr/bin/env python3

import json
import srsly
import textwrap

from typing import (
    Dict,
    Mapping,
)

# jsonable = json_serializable_or_repr


def yamlstr(obj: Mapping, prefix="got:\n", indent=5):
    return prefix + textwrap.indent(
        srsly.yaml_dumps(json_serializable_or_repr(dict(obj))),
        indent * " ",
    )


def json_serializable_or_repr(obj: Mapping, content=True) -> Dict:
    """Return dictionary without JSON non-serializable items.

    Parameters
    ----------
    obj : Mapping
        Mapping (e.g., dictionary or dict-like object) to be parsed.
    content : bool
        Replace unserializable data with its string representation.
        If ``False`` use type description instead.

    Returns
    -------
    Dict
        Parsed dictionary.

    Examples
    --------

    >>> from nvm.aux_srsly import json_serializable_or_repr as jsonable
    >>> import numpy as np
    >>> import srsly
    >>> import textwrap
    >>>
    >>> dict0 = dict(
    >>>     check="yes",
    >>>     items=list([1, 2, 3, "a", "b", "c"]),
    >>>     test=np.linspace(42, 44, 10),
    >>>     )
    >>> print(
    >>>     f"METADATA:\\n{textwrap.indent(srsly.yaml_dumps(jsonable(dict0)), '   ')}"
    >>> )
    METADATA:
       check: yes
       items:
         - 1
         - 2
         - 3
         - a
         - b
         - c
       test: "[42. 42.22222222 42.44444444 42.66666667 42.88888889 43.11111111\\n\\
         \\ 43.33333333 43.55555556 43.77777778 44.]"
    >>>
    >>> content = False
    >>> print(
    >>>     f"METADATA:\\n{textwrap.indent(srsly.yaml_dumps(jsonable(dict0, content=content)), '   ')}"
    >>> )
    METADATA:
       check: yes
       items:
         - 1
         - 2
         - 3
         - a
         - b
         - c
       test: '<<non-serializable: ndarray>>'


    """

    def default(o):
        return f"{o}" if content else f"<<non-serializable: {type(o).__qualname__}>>"

    return json.loads(json.dumps(obj, default=default))
