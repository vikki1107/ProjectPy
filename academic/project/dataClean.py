#!/usr/bin/env python
"""
This script will take the uncleaned joblist file and cleans the data within it by removing unnecessary fields and 
store it under a new file which will be used for data visualization

Author: Vivek
"""

import re

# Open a new file to store the data after removing all the characters mentioned below
with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs1.txt","w") as f_out:
    with open("E:\CSUEB\Courses\MGMT6160\Project\jobs_VK.txt","r") as f:
        for line in f:
            for ch in ['[', ']', '"', '\'']:
                line = line.replace(ch, '')
                line = re.sub(r',$', '', line, re.MULTILINE)
            f_out.write(line)

# Opens another new file to prepare the data based on title
with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs2.txt","w") as f_out:
    with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs1.txt","r") as f:
        for line in f:
            a = line.split(',')[0].lower()
            if 'data' in a or 'analyst' in a or 'analytics' in a or 'analysis' in a or 'intelligence' in a or 'quantitative' in a \
            or 'scientist' in a:
                f_out.write(line)

# Opens a file to replace the FT and PTs assuming FT and PT abbr. are only used only for full time and part time
# If there is any abbr as PT/FT in skills then that will be as well be replaced.
with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs3.txt","w") as f_out:
    with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs2.txt","r") as f:
        for line in f:
            line = line.replace("FT","Full-time")
            line = line.replace("PT","Part-time")
            f_out.write(line)
