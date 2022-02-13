import shutil
import os  
os.system('git config --global user.email "you@example.com"')
os.system('git config --global user.name "GitHub Actions"')
print("Script Started")
path = input("Where is your archives?\n A) A different directory\n B) In the running directory ")
if path == "A" or "a":
    runDir = input("Where is the directory (Please use fullpath(C:/examplefol1/examplefol2/)")
    FilesInCWD = False
    CWD = os.getcwd()
if path == "B" or "b":
    FilesInCWD = True
    runDir = os.getcwd()
gitQ = input("Is this from the TheSJWarriorArchive git repo?\n Yes or No?")
if gitQ == "yes" or "Yes":
     if FilesInCWD == False:
         filetree = os.listdir(runDir)
         shutil.copytree(filetree, CWD)
     if FilesInCWD == True:
         None
if gitQ == "no" or "No":
    gitURL = "https://github.com/tajt-passerby/TheSJWarriorArchive/"
    if FilesInCWD == True:
        gitrepo = 'TheSJWarriorArchive'
        gitcommit = os.system('git clone ' + gitURL)
        gitcommit
        gitQ_FT = os.listdir(runDir)
        filetree = os.listdir(runDir)
        shutil.copytree(filetree, gitrepo)
        runDir = gitrepo
        os.chdir(runDir)
    if FilesInCWD == False:
        repodir = input("Where would you like your git repo? (Please use fullpath)")
        gitcommit = os.system('git clone ' + gitURL + " " + repodir)
        gitcommit
        gitQ_FT = os.listdir(runDir)
        filetree = os.listdir(runDir)
        shutil.copytree(filetree, repodir) 
        runDir = repodir
        os.chdir(runDir)
list_ = os.listdir(runDir)
for file_ in list_:
    name, ext = os.path.splitext(file_)
ext = ext[1:]
if ext == 'png':
    os.system('git add {ext}')
    os.system("git commit -m 'update file'")
if ext == 'jpeg':
    os.system('git add {ext}')
    os.system("git commit -m 'update file'")
if ext == 'jpg':
    os.system('git add {ext}')
    os.system("git commit -m 'update file'")
if ext == 'mp4':
    os.system('git add {ext}')
    os.system("git commit -m 'update file'")
if ext == 'mov':
    os.system('git add {ext}')
    os.system("git commit -m 'update file'")
print("done")