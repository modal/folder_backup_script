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
#1.  Set the archive type
#2.  Set folder name of directory t to archive.
#    This folder must reside in the current directory
#3.  Set the paths to copy list
#
#Prequisites:
#   7-zip must be installed with command line path set correctly.
######################################################################

arc_type_str = "zip"    #zip, 7z, ...

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
zip_name = folder_name + date_used + ".zip"
zip_cmd = "7z a -t" + arc_type_str + " -mx9 " + zip_name + " " + folder_2_zip
os.system(zip_cmd)

#copy zip file to specific directories
copy_str = "copy " + zip_name
for path_2_copy in paths_2_copy:
    createPath(path_2_copy)
    print "Copying " + zip_name + " to " + path_2_copy
    shutil.copy2(zip_name, path_2_copy)

#delete zip file
print "Deleting " + zip_name
os.remove(zip_name)
