from io import StringIO
import sys
data = u"""4
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>"""
sys.stdin = StringIO(data)