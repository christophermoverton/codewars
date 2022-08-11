import sys
import xml.etree.ElementTree as etree
import testcase_study24
count = 0
def get_attr_number(node):
    # your code goes here
    count = 0
    count += len(node.attrib)
    for child in node:
        count+= get_attr_number(child)
    return count 
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))