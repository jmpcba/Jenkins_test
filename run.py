import os
#python script that will be run from jenkins

lines = ['/usr/bin/python\n', '\n', 'print "este es un artefacto"']
file_path = os.path.join(os.environ['WORKSPACE'],'artefacto.txt')
try:
    os.remove(file_path)
except FileNotFoundError as e:
    print e.message

print "hello GIT"

with open(file_path, 'w') as f:
    for line in lines:
        f.write(line)
    
