# -*- coding: utf-8 -*-
timezone=[]
timerange=[]
center=[]


with open("time.txt") as fp:
    cnt = 0
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if cnt is 0:
            cnt +=1
            timezone.append(line)
        elif cnt is 1:
            cnt+=1
            timerange.append(line)
        else:
            cnt = 0
            center.append(line)


for i in range(len(timezone)):

    print "<tr>"
    print "     <td>%s</td>"%(timezone[i])
    print "     <td>%s</td>"%(timerange[i])
    print "     <td>%s</td>"%(center[i])
    print "</tr>"