import os

def load_folder(data='',folder='',file_ext='',):
	print(f'[+] Loading {data}...')

	try:
		listdir = os.listdir(folder)
	except:
		print(f'[!] No {data.lower()} folder found\n[+] Creating Folder "{folder}"')
		os.mkdir(folder)
		listdir=[]

	dirs = []
	full_dirs = []

	if len(listdir) > 0:
		for l in listdir:
			if os.path.isfile(os.getcwd() + f'\\{folder}\\' + l) and l[len(file_ext)*-1:] == file_ext:
				print(f'      > {l}')
				dirs.append(l)
		print(f'[+] {data} Loaded!')
	else:
		print(f'[-] No {data} Found!')

	for d in dirs:
		full_dirs.append(folder + '\\' + d)

	return dirs, full_dirs

if __name__ == "__main__":
	# Load Data
	print('[+] Loading Data...')
	icons, icon_dirs = load_folder(data='Icons',folder='icons',file_ext='.ico')
	print('[+] Data Loaded!')