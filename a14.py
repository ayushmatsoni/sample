def nlines(f,n):
    with open(f, encoding="utf8") as file:
        print("LAST ",n,"LINES FROM FILE-->: ",f)
        print("")
        for line in (file.readlines()[-n:]):
            print(line,end='')
n=int(input("ENTER THE NO. OF LINES"))
name="textdemo.txt"
nlines(name,n)
#except:
 #   print("ERROR")
print("")

with open("textdemo.txt", encoding="utf8") as file:
    file.seek(0,0)
    wordstring=file.read()
    wordlist=wordstring.split(" " or "." or "," or ".\n" or "'s ")
i=0
count=0
for i in range(0,len(wordlist)):
    print("TOTAL "+wordlist[i]+"'s IN FILE-->%d"%int(wordlist.count(wordlist[i])))

print("")
try:
    f1=open("textdemo.txt", encoding="utf8")
    f2=open("textdemo2.txt","r+")
    f2.writelines(wordstring)
    f1.close()
    f2.close()
    print("COPY OPERATION PERFORMED")
except Exception:
    print("ERROR")


f1 = open("name.txt", "r+")
f2 = open("name2.txt", "r+")
print("COMBINED LINES-->")
for line1, line2 in zip(f1,f2):
    print(line2+line1,end="")
f1.close()
f2.close()

print("")
i=0
randomlist=[]
import random
for i in range(0,10):
    randomlist.append(random.randrange(0,100))
    randomlist[i]=str(randomlist[i])
print(randomlist)
print(sorted(randomlist))
f1=open("demo3.txt","r+")
f1.writelines(randomlist)
print(f1.readline())
print("read")
#print(l)
#for i in range(0,10):
#l2=sorted(l2)
#print(l2)
f1.close()
f1=open("sortedfile.txt","r+")
f1.writelines(sorted(randomlist))
print(f1.readline())