"""
Print in terminal with colors

Based in http://stackoverflow.com/a/34443116 and http://stackoverflow.com/a/17064509
"""

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'


def trace(text):
    print(GREEN + "{}".format(text) + ENDC)


def info(text):
    print(BLUE + "{}".format(text) + ENDC)


def warn(text):
    print(YELLOW + "{}".format(text) + ENDC)


def err(text):
    print(RED + "{}".format(text) + ENDC)
