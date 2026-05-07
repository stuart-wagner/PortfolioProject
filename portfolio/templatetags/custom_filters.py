from django import template

register = template.Library()


@register.filter
def split(value, separator):
    """
    Split a string by the specified separator.
    Usage: {{ value|split:"," }}
    """
    if value:
        return value.split(separator)
    return []


@register.filter
def strip_spaces(value):
    """
    Strip whitespace from a string.
    Usage: {{ value|strip_spaces }}
    """
    if value:
        return value.strip()
    return value
