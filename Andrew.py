

def main(name):
    i=0
    flag1=0
    flag2=0
    buf=0
    for x in name:
        if(i==0):
            buf=int(x)
            i+=1
            continue
        #print(str(int(x))+" "+str(buf))
        if(int(x)<=buf):
            flag1=1
        if(int(x)>=buf):
            flag2=1
        buf=int(x)
    if(flag1==0):
        return "Increasing"
    if(flag2==0):
        return "Decreasing"
    if((flag1==1)&(flag2==1)):
        return "Does not have properties"

try:
    name_input="input.txt"
    name_output="output.txt"
    #name_input=input("Name of input file:")
    #name_output=input("Name of output file:")
    file=open(name_input)
    answer=main(file)
    output=open(name_output,"w")
    output.write("Answer:"+answer)
finally:
    file.close()
    output.close()



            
    
