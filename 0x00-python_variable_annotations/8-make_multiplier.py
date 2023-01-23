#!/usr/bin/env python3

"""Returns a function that multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """Returns a float multiplied by multiplier"""
        return n * multiplier
    return multiply
