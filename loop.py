import os
from PCRT import PNG

directory = 'D:\NeuerOrdner'
for filename in os.listdir(directory):
	if filename.endswith(".png"):
		#print(os.path.join(directory, filename))
		#print(os.path.join(directory, '_' + filename))
		#print directory
		#print filename
		my_png=PNG(os.path.join(directory, filename),os.path.join(directory, '_' + filename),choices='y',mode=1)
		my_png.CheckPNG()
