# -*- coding: utf-8 -*-

"""
A global register to keep track of element behavior
"""

_highlight_element = False


def set_highlight(state):
    global _highlight_element
    _highlight_element = state


def highlight_state():
    global _highlight_element
    return _highlight_element
