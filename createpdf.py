import shutil
import os
srcdir = "./"

for src_file in os.listdir(srcdir) :
    if src_file.endswith ('pdf') :
        shutil.copy(srcdir + src_file, srcdir + "TI" + src_file)
