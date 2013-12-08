import os
import random
import sys
import shutil


if len(sys.argv) < 2:
    print 'usage: '+sys.argv[0]+' FILE [repeats] [FILE_TO_MIX]'
    sys.exit()

r = 14
b = 0
c = 1
fsize = os.path.getsize(sys.argv[1])
name = sys.argv[1].split('.')
while os.path.isfile(name[0]+str(c)+'.'+name[1]):
    c=c+1
shutil.copy2(sys.argv[1],name[0]+str(c)+'.'+name[1])

f = open(name[0]+str(c)+'.'+name[1],'rb+')

if len(sys.argv) > 2:
    r = int(sys.argv[2])

if len(sys.argv) > 3:
    bsize = os.path.getsize(sys.argv[3])
    b = open(sys.argv[3])

print 'Processing file '+sys.argv[1]+', output file: '+name[0]+str(c)+'.'+name[1]+', processing cycles: '+str(r)

for i in range(r):
    ss = random.randint(1,3)
    
    f.seek(random.randint(100,fsize-ss-1))
    if b != 0:
        b.seek(random.randint(30,fsize-ss-1))
        buf = b.read(ss)
    else:
        buf = f.read(ss)


    f.seek(random.randint(100,fsize-ss-1))
    f.write(buf)

f.close()
