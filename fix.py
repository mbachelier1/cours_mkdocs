import os, re

files = []

dirlist = ['docs\\']

while len(dirlist) > 0:
	for (dirpath, dirnames, filenames) in os.walk(dirlist.pop()):
		dirlist.extend(dirnames)
		ext = map(lambda n: os.path.join(*n), zip([dirpath] * len(filenames), filenames))
		ext = [x for x in ext if x[-3:] == '.md']
		files.extend(ext)

for file in files:
	with open(file, 'rt', encoding='utf8') as rf:
		buff = rf.readlines()
		new_buff = list()
		for line in buff:
			new_line = re.sub('\.\./', '', line, 1)
			new_buff.append(new_line)
	with open(file, 'wt', encoding='utf8') as wf:
		wf.writelines(new_buff)


