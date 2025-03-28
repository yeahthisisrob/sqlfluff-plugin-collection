from sqlfluff.core.plugin import hookimpl
from typing import List, Type
from sqlfluff.core.rules import BaseRule


@hookimpl
def get_rules() -> List[Type[BaseRule]]:
    """Return all rules from this plugin."""
    from .rules.rule_sqlfluffplugins_vf01_vertical_formatting import (
        Rule_SqlfluffPlugins_VF01,
    )

    return [Rule_SqlfluffPlugins_VF01]
