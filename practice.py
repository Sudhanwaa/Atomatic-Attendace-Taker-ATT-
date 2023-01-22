f=open('x.txt','w')
f.write("Hi")
f.close()
import os 
if os.stat("x.txt").st_size==0:
  print("Sudi")
else:
  print("Bokade")
  