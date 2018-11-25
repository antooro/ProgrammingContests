import numpy
with open('level1_3.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content.pop(0)
l = []
for i in content:
    l.append(i.split(' '))

arry = numpy.array(l)
nums = []
for (x,y),value in numpy.ndenumerate(arry):
    if (int(value)) not in nums and int(value)>0:
        nums.append(int(value))
e = (sorted(nums))
if len(e)==0:
    e = [0]
for n in e:
    print (n,end = ' ')
