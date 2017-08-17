#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

init_file_name = 'tmp\A.txt'
max_line = 5000000
if len(sys.argv) == 3:
    init_file_name = sys.argv[1]
    max_line = int(sys.argv[2])

file_count = 0
url_list = []

with open(init_file_name) as f:
    for line in f:
        url_list.append(line)
        if len(url_list) < max_line:
            continue
        file_name = "tmp\\"+str(file_count)+".txt"
        with open(file_name, 'w') as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list = []
            file_count+=1
if url_list:
	file_name = "tmp\\"+str(file_count)+".txt"
	with open(file_name, 'w') as file:
		for url in url_list:
			file.write(url)
print('done')
