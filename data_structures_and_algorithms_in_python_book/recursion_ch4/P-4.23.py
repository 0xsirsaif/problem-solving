"""
Implement a recursive function with signature find(path, filename) that
reports all entries of the file system rooted at the given path having the
given file name.
"""
import os

def find(path, filename):
    def _recur(entry):
        if os.path.isdir(entry):
            dirs = os.listdir(entry)
            for instance in dirs:
                instance_child = os.path.join(entry, instance)
                _recur(instance_child)
        elif entry.split('/')[-1] == filename:
            print(entry)
    return _recur(path)

print(find("/media/data/problem-solving/", 'R-4.7.py'))
