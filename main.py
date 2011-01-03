import sys
from myhtml import *
from util import *
from bibtex import *

url = sys.argv[1]

elems = extract_htmlelements(url)

#print(elems['title'])

printbibtex(url=url, author=elems['author'], title=elems['title'])
