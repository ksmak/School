# Python
import random


def get_activation_code(code_len: int):
    """Function for generate activate code."""
    digits = '0123456789'
    alfabet = 'ABCDEFGHJKLMNOPQRSTVWXYZ'
    specs = '@#%$'
    symbols = digits + alfabet + specs
    code = [symbols[random.randrange(0, len(symbols))] for _ in range(code_len)]
    return ''.join(code)