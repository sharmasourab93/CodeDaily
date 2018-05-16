class Point:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y

def onsegment(p,q,r):
    if (q.x<=max(p.x,r.x) and q.x>=min(p.x,r.x)) and (q.y<=max(p.y,r.y) and q.y>=min(p.y,r.y)):
        return True
    return False
def orientation(p,q,r):
    val=((q.y-p.y)*(r.x-q.x))-((q.x-p.x)*(r.y-q.y))
    if val==0: return 0
    if val==1: return 1
    else: return 2
def doIntersect(p1,q1,p2,q2):
    o1=orientation(p1,q1,p2)
    o2=orientation(p1,q1,q2)
    o3=orientation(p2,q2,p1)
    o4=orientation(p2,q2,q1)

    if o1!=o2 and o3!=o4: return True
    if o1==0 and onsegment(p1,p2,q1): return True
    if o2==0 and onsegment(p1,q2,q1): return True
    if o3==0 and onsegment(p2,p1,q2): return True
    if o4==0 and onsegment(p2,q1,q2): return True
    return False

def main():
    p1=Point(1,1)
    q1=Point(10,1)
    p2=Point(1,2)
    q2=Point(10,2)
    if doIntersect(p1,q1,p2,q2) is True: print("Yes")
    else: print("No")

    p1 = Point(10,0)
    q1 = Point(0, 10)
    p2 = Point(0,0)
    q2 = Point(10,10)
    if doIntersect(p1, q1, p2, q2):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()