a=open("demo.txt","w")
a.write("asdfghjk")
a.close()
b=open("demo.txt","a")
b.write("wertyuio")
b.close()
c=open("demo.txt","r")
print(c.read())
c.close()
d=open("demo.txt","w")
d.write("asdfghj")
d.close()
e=open("demo.txt","r")
print(e.read())
e.close()
f=open("demo.txt","r")
for x in f:
    print(x)
f.close()
import os
os.remove("demo.txt")


import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("the file is does not exist")



