#concatination of three strings
a="the"
b="elephant"
c="is big"
d=a+" "+b+" "+c
print("the concatination of three strings:",d)
#using the f string
print(f"concatination of the strings:{a} {b} {c}")
#using formatmethod
print("{} {} {}".format(a,b,c))
#using joinmethod
print(" ".join([a,b,c]))