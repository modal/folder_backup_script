
import os
import time
import shutil

######################################################################

#folder to zip up
folder_name = "ahv_clk_gen"
folder_2_zip = folder_name+"\""

#Copy Directory List
paths_2_copy = [
    r"S:\R_D\PN Tech\CRE-B\firmware\ahv_clk_gen",
    r"R:\backup\CRE-B\firmware\ahv_clk_gen"]

#Move Directory
paths_2_move = []

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
#move_str = "move " + zipped_name

for path_2_copy in paths_2_copy:
    createPath(path_2_copy)
    print "Copying " + zipped_name + " to " + path_2_copy
    shutil.copy2(zipped_name, path_2_copy)
    #DONT USE os.system("\"" + copy_str + "\" " + path_2_copy)

#paths_2_move = "\"R:\\backup\cre_hub_processor\cre_hub\""
#print "Moving " + date_used + ".zip to " + " " + paths_2_move
#os.system(move_str + " " + paths_2_move)

#FIXME If not moving delete zip file?
if paths_2_move == []:
    print "Deleting " + zipped_name
    delete_str = "del " + zipped_name
    os.system(delete_str)

#Basic Bash Script
#echo "ZIP UP NGPNT_HUB"
#7z a -tzip 2010_12_22.zip ngpnt_hub\
#copy 2010_12_22.zip "S:\Ngpnt Project\Updates\Backup Tim Dahlin\cre_hub_processor\cre_hub\"
#move 2010_12_22.zip  "R:\backup\cre_hub_processor\cre_hub\"
