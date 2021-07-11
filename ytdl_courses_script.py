## MAKE SURE youtube-dl.exe IS IN YOUR ENVIRONMENT PATH!
import os	
import subprocess
import tqdm

PATH=os.getcwd()
os.chdir(PATH)
YTDL_PATH=""

for fname in os.listdir(os.getcwd()):
    if fname.endswith('.txt'):
        # do stuff on the file
        URL_LIST_FILE=fname
        break		
else:
    # do stuff if a file .true doesn't exist.
	URL_LIST_FILE=input("Name of file with list:\t") #enter path or just the name if you are in the same folder
	
NAME_OF_COURSE=URL_LIST_FILE.replace('.txt',"") #enter path or just the name if you are in the same folder
NAME_OF_COURSE=NAME_OF_COURSE.strip()
NAME_OF_COURSE=NAME_OF_COURSE.replace(" ","_")

check_ytdl=subprocess.getoutput('youtube-dl.exe')
if "not recognized" in check_ytdl:
	if os.path.isfile("youtube-dl.exe"):    # case youtube-dl isn't on ENVIRONMENT VARIABLES but is in the folder
	    YTDL_PATH=os.path.abspath("youtube-dl.exe")
	else:
	    print("You are missing youtube-dl.exe or it isn't configured in your environment path properly.\nPlease fix and try again.")
	    exit(0)

else:
	print("youtube-dl.exe is valid")


lines=[]
with open(URL_LIST_FILE) as f:
    lines=(f.readlines())
	
# Parse and configure youtube-dl command
newlines=[]
for i, line in enumerate(lines):
	# youtube-dl.exe --newline -i -f mp4 --ignore-config --hls-prefer-native "{}" -o {}_{}.mp4\n'.format(str(lines[i].strip()),NAME_OF_COURSE,i))
	if (len(line)<5): # ignore empty lines
	    continue
	if len(YTDL_PATH)>0:  # case youtube-dl isn't on ENVIRONMENT VARIABLES but is in the folder
		newlines.append('{} --newline -i -f mp4 --ignore-config --hls-prefer-native "{}" -o {}_{}.mp4\n'.format(YTDL_PATH,str(lines[i].strip()),NAME_OF_COURSE,i))
	else:  # best case- youtube-dl is installed properly.
	    newlines.append('youtube-dl.exe --newline -i -f mp4 --ignore-config --hls-prefer-native "{}" -o {}_{}.mp4\n'.format(str(lines[i].strip()),NAME_OF_COURSE,i))

# Create bat file for easy sharing	
output_filename="URL_list_for_{}.bat".format(NAME_OF_COURSE)
print("Downloading:\n\n")
with open(output_filename, 'w') as f:
	for item in tqdm.tqdm(newlines):
		f.write("%s" % item)		
f.close()

# execute commands
for item in tqdm.tqdm(newlines):
		os.system(item)
		
print("\n##############################\nDONE\n##############################")