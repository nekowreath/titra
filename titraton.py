from pathlib import Path
from pathlib import PurePath
import pandas as pd
import os
import re

current = Path.cwd()
print(current)
p=Path(current)

print(p)

dir_list=list(p.glob('**/*.csv'))
path_w =p / 'test_w.txt'

for filename in dir_list:
	with open(filename, 'r') as input, open(path_w, mode='a') as f:

		f.write('\n')	
#		readtext=input.read()
#		#print(readtext.split(','))
#		if readtext.find("name") >= 0:
#			print(readtext[:-1])

		for line in input:


			if line.startswith("Comment"):
	#			print(line[:-1])

				with open(path_w, mode='a') as f:
				    f.write(line[:-1])
				    f.write(",")
	#			with open(path_w) as f:
	#			    print(f.read())

			strline=str(line)
			val=re.search('[0-9]+\.[0-9]+',strline)
			if val :

				with open(path_w, mode='a') as f:
				    f.write(val.group())
				    f.write(",")
	#			with open(path_w) as f:
	#			    print(f.read())

	#			print(val.group())

		
col_names = [ 'c{0:02d}'.format(i) for i in range(10) ]
df = pd.read_csv('./test_w.txt', sep=',', names=col_names)
#print(df.head(3))
df_s = df.sort_values('c00')
dff=df_s.drop("c00",axis=1)

dff.iat[0,0]=0

print(dff)
print(dff.diff(axis=0))

#print(df_s)

#df = pd.concat([df_s]*10**5, ignore_index=True)



#os.remove(path_w)
		#	if line.find("name") >= 0:
		#		print(line[:-1])
				#if line.startswith("a"):
				#	print(line[:-1])
#				print(str(line))



#dff=df.read_csv(df)
#print(dff)
#
#print(df)
#
#for files in dir_list:
#	print(files)


#with p.open() as f:
#	f.readline()
#	print(f.readline())

#
