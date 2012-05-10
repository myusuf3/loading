
"""
loading

simple loading bar in python

"""
import sys

class Loading(object):
    """Loading bar class."""

    def __init__(self, full, loading_message='loading...', load_char='#'):
        self.start = 0
        self.write = sys.stdout
        self.full = full
        self.load_char = load_char
        self.write.write('\n' + loading_message +'\n')

    def complete(self, part):    
        part = min(part, self.full)

        if self.full:
            progress = int(round(100.0*part/self.full))
            if progress < 1: progress = 1
        else:
            progress=100

        start = int(progress/2)
        if start <= self.start:
            return

        for i in range(self.start, start):
            # write one more char for range
            # between previous and now
            self.write.write(self.load_char)
        self.write.flush()
        self.start = start
        if progress == 100:
            self.write.write("\n")