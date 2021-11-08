import glob, os
import shutil
import mouse

fromdir = r"D:\Unreal Engine Testing\Engine\Source"
actualldir = r"C:\Program Files\Epic Games\UE_4.25\Engine\Source"
todir = r"D:\Unreal Engine Testing\Deleted Stuff\Plugins"
sourcetodir = r"D:\Unreal Engine Testing\Deleted Stuff\Source Removed Files"
logfile = r"C:\Users\Haven_Remix\Desktop\Scripts\PrecompiledExtensions.txt"

filenumber = 0

foundextensions = []

if True:
    os.chdir(fromdir)
    
    

elif False:
    os.chdir(actualldir)
    for file in glob.glob("**/*.*", recursive=True):
        filenumber+=1

        filename, fileextension = os.path.splitext(file)
        #print(fileextension)

        if fileextension not in foundextensions:
                foundextensions.append(fileextension)
                print(foundextensions)
    with open(logfile, "w") as f:
        for item in foundextensions:
            f.write("%s\n" % item)

