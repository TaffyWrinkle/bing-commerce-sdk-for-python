# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class LogicalOperator(str, Enum):

    and_enum = "And"
    or_enum = "Or"


class EquivalenceOperator(str, Enum):

    eq = "Eq"
    ne = "Ne"


class ComparisonOperator(str, Enum):

    eq = "Eq"
    ne = "Ne"
    gt = "Gt"
    lt = "Lt"
    ge = "Ge"
    le = "Le"


class CategoryOperator(str, Enum):

    in_enum = "In"
    not_in = "NotIn"


class SetOperator(str, Enum):

    in_enum = "In"
    not_in = "NotIn"
