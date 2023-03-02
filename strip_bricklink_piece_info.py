#!/bin/python3

import html_to_json
import json

bricklink_list = open('bricklink_list.txt', 'r')
bricklink_list_str = bricklink_list.read()
bricklink_list_json = html_to_json.convert(bricklink_list_str)

colors = []

for i in range(1, len(bricklink_list_json['span']) // 2):
    index = i * 2
    bkg_obj = bricklink_list_json['span'][index]
    dtl_obj = bricklink_list_json['span'][index + 1]

    color = bkg_obj['_attributes']['style'].split('#')[1]
    name = dtl_obj['a'][0]['_value']
    count = int(dtl_obj['_value'].strip('()'))

    colors += [(color, name, count)]

output = open('pieces.json', 'w+')
output.write(json.dumps(colors, indent = 2))
