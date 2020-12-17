import random
def gennum():
    x=""
    j=random.randint(0,9)
    for i in range(4):
        while(str(j) in x):
            j=random.randint(0,9)
        x+=str(j)
    return x
def checknumber(n):
    for i in n:
        if(n.count(i)>1 or len(n)!=4):
            return False;
    return True;
def game(n):
    num=gennum()
    cnt_c=0
    cnt_b=0;
    while(True):
        if(checknumber(n)):
            for i in range(4):
                for j in range(4):
                    if(i==j and n[i]==num[i]):
                        cnt_b+=1;
                    elif(i!=j and n[i]==num[j]):
                        cnt_c+=1
                    else:
                        continue;
            if(cnt_b==4):
                cnt_b=0;cnt_c=0;
                return True;
            else:
                print(str(cnt_b)+"B "+str(cnt_c)+"C")
                cnt_b=0;cnt_c=0;
                n=input();
        else:
            print("enter correct number with random digits size must be 4")
            n=input();
n=input()
if(game(n)):
    print("You have won");