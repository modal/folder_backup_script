import os
import time
import shutil
######################################################################
#Description:
#This script zips a folder in the current directory and copies the
#zip file to the specified paths.  Once all copying is complete the 
#zip file is deleted.
#
#Configuration Steps
#1.  Set folder name in the directory you want to s
#2.  Set the copy
#
#Prequisites:
#   7-zip must be installed with path set correctly.
######################################################################

#folder to zip up
folder_name = "FOLDER_NAME"
folder_2_zip = folder_name+"\""

#Copy Directory List
paths_2_copy = [
    r"S:\PATH_NAME",
    r"R:\PATH_NAME"]
######################################################################
def createPath(path):
    if not os.path.isdir(path):
        print "Creating directory for " + path
        os.mkdir(path)
######################################################################
date_used = time.strftime("%Y_%m_%d")
print date_used

#zip up the specified folder
zipped_name = folder_name + date_used + ".zip"
zipstr = "7z a -tzip " + zipped_name + " " + folder_2_zip
os.system(zipstr)

#copy and move zip file to server or different directory
copy_str = "copy " + zipped_name

for path_2_copy in paths_2_copy:
    createPath(path_2_copy)
    print "Copying " + zipped_name + " to " + path_2_copy
    shutil.copy2(zipped_name, path_2_copy)

print "Deleting " + zipped_name
os.remove(zipped_name)
