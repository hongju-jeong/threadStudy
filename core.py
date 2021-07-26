import subprocess
from glob import glob

filelist = glob("repeat.py")
print(filelist)
for file in filelist:
    subprocess.call(['python',file])