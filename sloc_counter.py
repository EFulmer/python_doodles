import re
import sys

def python_sloc(src, count_whitespace=True):
    """
    Returns number of non-comment lines of code in src. 
    If whitespace=False, whitespace lines are not counted either.
    """

    if count_whitespace:
        python_comments = re.compile('\s*#')
    else:
        python_comments = re.compile('^\s*$')

    with open(src, 'r') as f:
        lines = f.readlines()
        return sum([1 for l in lines if not re.match(python_comments, l)])


# TODO: Ruby (should be the same?), Perl (as Ruby?), C, C++, Java, 
# OCaml, Haskell, Lisp, Visual Basic
