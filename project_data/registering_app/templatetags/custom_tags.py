from django import template

register = template.Library()

def adds100(value):
    """
    Adds 100 to the value
    """
    return value + 100

register.filter("adds100", adds100)

