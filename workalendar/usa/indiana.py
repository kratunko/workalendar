# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .core import UnitedStates, WashingtonsBirthdayInDecemberMixin


class Indiana(UnitedStates, WashingtonsBirthdayInDecemberMixin):
    """Indiana"""
    include_good_friday = True
    include_thanksgiving_friday = True