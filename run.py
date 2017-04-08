import os
#python script that will be run from jenkins

lines = ['/usr/bin/python\n', '\n', 'print "este es un artefacto"']

try:
    os.remove('artefacto.txt')
except FileNotFoundError as e:
    print e.message

print "hello GIT"

with open('artefacto.txt', 'w') as f
    for line in lines:
        f.write(line)
    
