from atexit import register
from tkinter.tix import Tree
from unicodedata import name
from django import template
from customers.models import *

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(cart_item, user):
    is_present = Cart.objects.filter(user=user, post=cart_item).exists()
    if is_present:
        return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(cart_item_id, user):
    is_present = Cart.objects.filter(user=user, post=cart_item_id)
    quantity = 0
    for i in is_present:
        quantity = quantity + i.quantity
    return quantity