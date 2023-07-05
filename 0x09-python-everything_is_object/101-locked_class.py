#!/usr/bin/python3
"""Defines a lockedclsss representation"""


class LockedClass:
    """
    Prevents the creation of new instance attribute except
    for the attribute 'first_name'.

    Attributes:
        __slots__ (list): A list of allowed instance attributes.
    """

    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        """
        Overrides the attribute assignment to control the creation
        of new instance attribute

        Args:
             attr (str): attribute name
             value: value to be assigned to attribute
        Raises:
            AttributeError: if attribute being set is not 'first_name'
        """
        if attr != 'first_name':
            raise AttributeError("No new instance attribute")
        else:
            object.__setattr__(self, attr, value)
