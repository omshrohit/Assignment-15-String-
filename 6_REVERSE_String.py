# write a python script to reverse a string(" iNeuron")
a="iNeuron"
print(a[::-1])


print("---USING LOGIC----")

for i in range(len(a)-1,-1,-1):
    print(a[i],end="")