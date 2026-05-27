"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""

import warnings

__all__ = [
    "CRAFTWarning",
    "CRAFTUserWarning",
    "CRAFTDeprecationWarning",
    "CRAFTPendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class CRAFTWarning(Warning):
    """
    The base warning class from which all IMPAX CRAFT warnings should inherit.

    Any warning inheriting from this class is handled by the IMPAX CRAFT
    logger. This warning should not be issued in normal code. Use
    "CRAFTUserWarning" instead or a specific sub-class.
    """


class CRAFTUserWarning(UserWarning, CRAFTWarning):
    """
    The primary warning class for IMPAX CRAFT.

    Use this if you do not need a specific type of warning.
    """


class CRAFTDeprecationWarning(FutureWarning, CRAFTWarning):
    """
    A warning class to indicate a deprecated feature.
    """


class CRAFTPendingDeprecationWarning(PendingDeprecationWarning, CRAFTWarning):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `CRAFTUserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, CRAFTUserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `CRAFTDeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, CRAFTDeprecationWarning, stacklevel + 1)
