import sys
from html_parser import HtmlToJson
args= sys.argv
if len(args)!=2:
    print('Incorrect argument(s)\nEnter: python <filename> <htmlfile>')
    exit(0)
with open(args[1], 'r') as f:
    json_op= HtmlToJson().parse(f)
    with open('json_result.json', 'w') as opf:
        print(json_op)
        opf.write(json_op)
