from operator import truediv
import random 
şifre1= random.randrange(10)
şifre2= random.randrange(10)
şifre3= random.randrange(10)
şifre4= random.randrange(10)
dizi=[ şifre1,şifre2,şifre3,şifre4]
print("şifremiz: "+str(şifre1)+str(şifre2)+str(şifre3)+str(şifre4))

while(True):
    tahmin=int(input("şifre tahmini giriniz: "))
    s1=int(tahmin/1000)
    s2=int((tahmin/100)%10)
    s3=int((tahmin/10)%10)
    s4=int(tahmin%10)
    tah= [s1,s2,s3,s4]
    yüzdelik=0
    if(şifre1==s1):
        print("*")
        yüzdelik+=25
        
    else:
        for i in dizi:
            if(s1==i):
                print("+")
                yüzdelik+=13
                break
        else:
            print("-")
    
    if(şifre2==s2):
        print("*")
        yüzdelik+=25
        
    else:
        for i in dizi:
            if(s2==i):
                print("+")
                yüzdelik+=13
                break
        else:
            print("-")
    
    if(şifre3==s3):
        print("*")
        yüzdelik+=25
        
    else:
        for i in dizi:
            if(s3==i):
                print("+")
                yüzdelik+=13
                break
        else:
            print("-")
    
    if(şifre4==s4):
        print("*")
        yüzdelik+=25
        
    else:
        for i in dizi:
            if(s4==i):
                print("+")
                yüzdelik+=13
                break
        else:
            print("-")
    
    
    if(tah==dizi):
        print("hedefe ulaima yüzdeliği: "+str(yüzdelik)+"%")        
        print("tebrikler")
        break
    print("hedefe ulaima yüzdeliği: "+str(yüzdelik)+"%")        


 