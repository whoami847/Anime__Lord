import os
import sys

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)
    return "Restarting the bot..."
