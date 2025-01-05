from enum import Enum

from pip._internal.utils.misc import enum


class DamageMods(enum):
    VULNERABLE = 1
    RESISTANT = 2
    IMMUNE = 3
