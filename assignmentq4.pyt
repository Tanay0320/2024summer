def checkpal():
    string=input("enter the string: ")
    n=len(string)
    string1=''
    
    for i in range (0,n):
        if(string[i].isalnum()==1):
            string1+=string[i]
    for j in range (0,len(string1)):
        flag=1
        if(string1[j]==string1[len(string1)-j-1]):
            continue
        else:
            flag=0
            break   
    if(flag==0):
        return False
    else:
        return True     
print(checkpal())