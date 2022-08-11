from io import StringIO
import sys
data = u"""hello   world  lol"""
sys.stdin = StringIO(data)