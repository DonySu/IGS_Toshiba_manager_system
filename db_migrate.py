#!flask/bin/python3

import os
import os.path
import re
from config import basedir_local

migration = basedir_local + '/migrations/versions'
print(migration)
v_str = []

for parent,dirnames,filenames in os.walk(migration):
    for filename in filenames:
        v = re.findall(r'([0-9]{4}){1}.py',filename)
        if v != []:
            v_str.append(int(v[0]))

def get_current_version():
    if len(v_str) == 0:
        current_version = 0
    else:
        current_version = max(v_str)
    return current_version

version_str = 'Version_' + '%04d'% (get_current_version()+1)
command = "flask/bin/python3 db_manage.py db migrate -m " + str(version_str)

os.system(command)

        
     
        
