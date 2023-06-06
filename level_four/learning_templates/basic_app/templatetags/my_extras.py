from django import template

register = template.Library()

@register.filter(name='try')
def try_me(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('try_me', try_me)