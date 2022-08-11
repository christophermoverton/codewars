from io import StringIO
import sys
data = u"""Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael"""
sys.stdin = StringIO(data)