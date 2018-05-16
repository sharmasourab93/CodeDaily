class Point:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y

def orientation(p,q,r):
    val=((q.y-p.y)*(r.x-q.x))-((q.x-p.x)*(r.y-q.y))
    if val==0: return 0
    if val==1: return 1
    else: return 2

def convexHull(points):
    #if len(points)<3: return None
    hull=[]
    l=0
    for i in range(1,len(points)):
        if points[i].x<points[l].x:
            l=i
    p=l
    q=0
    while True:
        hull.append(points[p])
        q=(p+1)%len(points)
        for i in range(len(points)):
            if (orientation(points[p],points[i],points[q])==2):
                q=i
        p=q
    for i in hull:
        print("Here")
        print("(",i.x,i.y,")")

def main():
    points=[Point(0,3),Point(2,2),Point(1,1),Point(2,1),Point(3,0),Point(0,0),Point(3,3)]
    convexHull(points)

main()