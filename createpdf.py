#!/usr/bin/python2.7
import shutil
import os
srcdir = "./"

# debut
for src_file in os.listdir(srcdir) :
    if src_file.endswith ('pdf') :
        shutil.copy(srcdir + src_file, srcdir + "TI" + src_file)
