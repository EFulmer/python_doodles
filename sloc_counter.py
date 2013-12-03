import re

def python_sloc(src, count_whitespace=True):
    python_comments = re.compile('\s*#')
    with open(src, 'r') as f:
        lines = f.readlines()
        return sum([1 for l in lines if not re.match(python_comments, l)])
