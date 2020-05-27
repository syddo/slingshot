# -*- coding: utf-8 -*-
"""
    Common Methods that can be shared accross projects.
"""

import getpass


def getUserName():
    """
    return the user currently logged in.
    """
    return(
        getpass.getuser()
    )
