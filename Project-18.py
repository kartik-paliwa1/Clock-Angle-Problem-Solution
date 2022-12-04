''' Python program to find angle
between hour and minute hands '''


def Clock_Angle(h,m):
    """Function to Calculate angle b/w
       hour hand and minute hand"""
    a,b,c=0,0,0
    if m==0:
        b=360
    if 0<= h <=12:
        a=h*30
        if m!=0 and h==12:
            a=0
        c=1
    elif 13<= h <=24:
        h-=12
        a=h*30
        if m!=0 and h==12:
            a=0
        c=1
    else: # validate the input
        print("invalid time")
    for i in range(m):
        a+=.5
        b+=6
    x=int(a)
    y=b
    if c==1:
        return abs(x-y)
        # Find the difference b/w two angles

h=int(input("enter hour :-"))
m=int(input("enter min :-"))
print("Angle -->",Clock_Angle(h,m))
    
