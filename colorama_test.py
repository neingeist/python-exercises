#!/usr/bin/env python
from __future__ import division, print_function

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Fore.RESET + Back.RESET + Style.BRIGHT + 'and in bright text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL + 'back to normal now')
