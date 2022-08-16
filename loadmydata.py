import os

def check_folder_exists(folder):
	for i in os.listdir(os.getcwd()):
		if i == folder: return True 
	os.mkdir(os.getcwd()+'\\'+folder)
	return False

def check_file_exists(filename='',path=''):
	for i in os.listdir(os.getcwd()+path):
		if i == filename: return True
	open(os.getcwd() + path + filename,'w')
	return False

def load_folder(data='',folder='',file_ext='',):
	print(f'[+] Loading {data}...')

	if check_folder_exists(folder):
		listdir = os.listdir(os.getcwd()+'\\'+folder)
	else:
		print(f'[!] No {data.lower()} folder found\n[+] Creating Folder "{folder}"')
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
