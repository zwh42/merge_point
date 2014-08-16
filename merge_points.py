import numpy as np
import scipy as sp
import pylab as pl
import math
from random import *
import os
import time





point = []

#pl.show()

#for i in range(10):
#    point.append({"x":randint(0,10),"y": randint(0,10),"used":False})
#    point.append({"x":randint(30,40),"y": randint(30,40),"used":False})
#    point.append({"x":uniform(25,35), "y":uniform(35,45),"used":False})
#    point.append({"x":uniform(90,100),"y":uniform(90,100),"used":False})
#    point.append({"x":uniform(75,85),"y":uniform(10,20),"used":False})
#    
#    point.append({"x":uniform(0,100),"y":uniform(0,100),"used":False})

x1 = [8, 10, 2, 8, 6, 0, 2, 4, 7, 1]
y1 = [6, 1, 1, 5, 5, 6, 10, 2, 8, 10]
x2 = [42, 43, 40, 41, 50, 43, 45, 40, 46, 41]
y2 = [43, 47, 41, 47, 43, 43, 42, 42, 41, 46]



#
for i in range(10):
    point.append({"x":x1[i],"y":y1[i],"used":False})
    point.append({"x":x2[i],"y":y2[i],"used":False})
    


    

for pt in point:
    #print "x =", pt["x"],"y =", pt["y"]
    pl.plot(pt["x"],pt["y"],"or")

pl.show()

        
boxes = []
#boxes.append([point.pop()])
print boxes
threshold = 3


###for pt1 in point:
###    table = []
###    table.append(pt1)
###    if pt1["used"] :
###        continue
###    for pt2 in point:
###        if pt2["used"]:
###            continue
###        #if  math.sqrt((pt1["x"] - pt2["x"]) ** 2 + (pt1["y"] - pt2["y"]) ** 2) <= threshold:
###        #    table.append(pt2)
###        #    pt2["used"] = True
###        for pt3 in talbe:
###            if  math.sqrt((pt3["x"] - pt2["x"]) ** 2 + (pt3["y"] - pt2["y"]) ** 2) <= threshold:
###            
##        
##            
#    boxes.append(table)


#for pt1 in point:
#    table = []
#    table.append(pt1)
#    if pt1["used"]:
#        continue
#    pt1["used"] = True
#    for pt2 in point:
#        
#        for pt3 in table:
#            if math.sqrt((pt3["x"] - pt2["x"]) ** 2 + (pt3["y"] - pt2["y"]) ** 2) <= threshold:
#                add_to_table = True
#                break
#        if add_to_table :
#            table.append(pt2)
#            pt2["used"] = True
#            add_to_table = False
#    boxes.append(table)
    

#for i in range(len(point)):
#    pt1 = point[i]
#    table = []
#    if pt1["used"]:
#        continue
#    table.append(pt1)
#    pt1["used"] = True
#    print "table before loop:", table
#    
#    for j in range(len(point)):
#        pt2 = point[j]
#        print "j before: ", j
#        if pt2["used"] :
#            continue
#                
#        add_to_table = False
#        for k in range(len(table)):
#            pt3 = table[k]
#            print "pt3(",pt3["x"],", ",pt3["y"],")"
#            print "pt2(",pt2["x"],", ",pt2["y"],")"
#            print "table in loop = ", table
#            if pt3 == pt2:
#                continue
#            distance = math.sqrt((pt3["x"] - pt2["x"]) ** 2 + (pt3["y"] - pt2["y"]) ** 2)
#            print "distance = ", distance
#            if distance <= threshold:
#                add_to_table = True
#                break
#        
#        print "j after ", j
#        
#        if add_to_table:
#            table.append(pt2)
#            pt2["used"] = True
#            add_to_table = False
#            print "table after append:", table
#            j = 0
#            print "reset j = ", j
#            #pl.plot(pt3["x"],pt3["y"], "vb")
#            #time.sleep(5)
#            #pl.show()
#            #pl.plot(pt2["x"],pt2["y"],"^b")
#            #time.sleep(5)
#            #pl.show()
#            
#            
#    
#    boxes.append(table) 
#            



i = 0
while i < len(point):
    pt1 = point[i]
    table = []
    if pt1["used"]:
        i = i + 1
        continue
    table.append(pt1)
    pt1["used"] = True
    print "table before loop:", table
    
    j = 0
    while j < len(point):
        pt2 = point[j]
        print "j before: ", j
        if pt2["used"] :
            j = j + 1
            continue
                
        add_to_table = False
        k = 0
        while k < len(table):
            print "k in k loop", k
            pt3 = table[k]
            print "pt3(",pt3["x"],", ",pt3["y"],")"
            print "pt2(",pt2["x"],", ",pt2["y"],")"
            print "table in loop = ", table
            if pt3 == pt2:
                k = k + 1
                continue
            distance = math.sqrt((pt3["x"] - pt2["x"]) ** 2 + (pt3["y"] - pt2["y"]) ** 2)
            print "distance = ", distance
            if distance <= threshold:
                add_to_table = True
                break
            k = k + 1
        
        print "j after ", j
        
        if add_to_table:
            table.append(pt2)
            pt2["used"] = True
            add_to_table = False
            print "table after append:", table
            j = 0
            print "reset j = ", j
        else:
            j = j + 1

            
            
    
    boxes.append(table)
    i = i + 1 
            



#print "boxes = ", boxes


#for pt in boxes[1]:
#    pl.plot(pt["x"],pt["y"],"vb")
#    
#for pt in boxes[2]:
#    pl.plot(pt["x"],pt["y"],"^y")
    

#for pt in boxes[0]:
#    pl.plot(pt["x"],pt["y"],"sb")

style = ["1","2","H", "v","*","p","h"]
color = ["b","g","c","m","y","k"]

i = 0
count = 0
for box in boxes:
    for pt in box:
        pl.plot(pt["x"],pt["y"],style[i%7]+color[i%6],markersize=5)
        count = count + 1
    i = i + 1


for box in boxes:
    left_x = min(pt["x"] for pt in box)
    left_y = min(pt["y"] for pt in box)
    right_x = max(pt["x"] for pt in box)
    right_y = max(pt["y"] for pt in box)
    print "min x = ", left_x, "min y = ",left_y, "max x = ",right_x,"max y = ", right_y, "\n";
    if left_x == right_x and left_y == right_y:
       pl.gca().add_patch(pl.Rectangle((left_x - 5,left_y - 5),10,10))
       #pass 
    else:         
        pl.gca().add_patch(pl.Rectangle((left_x,left_y),right_x - left_x,right_y - left_y))



pl.ylim([-1,101])
pl.xlim([-1,101])

pl.show()

print  "boxes = ", len(boxes), "point counts =" , count

#for pt1 in point:
#    for pt2 in point:
#        if pt1 != pt2:
#            distance = math.sqrt((pt1["x"] - pt2["x"]) ** 2 + (pt1["y"] - pt2["y"]) ** 2)
#            if distance <= threshold :
#                print "pt1 = ", pt1, "pt2 =",pt2, "distance = ", distance
#                if boxes == []:
#                    boxes.append()

#for pt1 in point:
#    for pt2_list in boxes:
#        for pt2 in pt2_list:
#            print pt2
#            distance = math.sqrt((pt1["x"] - pt2["x"]) ** 2 + (pt1["y"] - pt2["y"]) ** 2)
#            #print "pt1 = ", pt1, "pt2 =",pt2, "distance = ", distance
#            if distance < threshold:
#                print "before append list",pt2_list
#                pt2_list.append(pt1)
#                print "after append list",pt2_list
#                break
#            else:
#                boxes.append([pt1])
#                box_flag = True
#            
#            if box_flag:
#                box_flag = False
#                break
        
       
        
           
    
    
#
#
##pl.gca().add_patch(pl.Rectangle((x_left,y_left),x_legnth,y_length))
#pl.gca().add_patch(pl.Rectangle((10,20),30,40,edgecolor = "blue"))
#pl.show()