"""
Question:
    Find Relations between the given pair of names.
    For example:
    Jack,Joe
    Joe,Bill
    if Jack, Joe : print("Relation Ship found") Jack->Joe
"""
class Relations:
    def __init__(self):
        self.adjList=dict()
        self.friend=dict()
    
    def readCsv(self):
        file=open('friends.txt', "r+")
        for i in file.readlines():
            print()
            x=i.strip('\n').split(',')
            for j in x:
                self.friend.update({j:False})
        for i in self.friend:
            self.adjList.update({i:[]})
        #print(self.friend, self.adjList)
        file.close()
    
    def makeRelations(self):
        file=open('friends.txt', "r+")
        for i in file.readlines():
            x=i.strip('\n').split(',')
            self.adjList[x[0]].append(x[1])
            self.adjList[x[1]].append(x[0])
        #for k,v in self.adjList.items():
        #   print(k,"->",v)
        file.close()
    
    def findRelationsUtil(self,x,y):
        if y in self.adjList[x]:
            self.friend[x]=True
            self.friend[y]=True
            print(x,'->',y)
            return True
        
        for i in self.adjList[x]:
            self.friend[x]=True
            if self.friend[i] is False:
                self.friend[i]=True
                if y in self.adjList[i]:
                    self.friend[y]=True
                    return True
                else:
                    return self.findRelationsUtil(i,y)
            else:
                pass
                
        self.flagOffset()
        return False
            
    
    def printRelations(self,x,y):
        l=[]
        for k in self.friend:
            if self.friend[k] is True:
                if k is x or k is y:
                    pass
                else:
                    l.append(k)
        print('->'.join(l))
        
    def flagOffset(self):
        for k in self.friend:
            self.friend[k]=False
        
    def findRelations(self,x,y):
        if self.findRelationsUtil(x,y) is True:
            print("Relation Ship Found between {} and {}:".format(x,y))
            self.printRelations(x,y)
            self.flagOffset()
        else:
            print("\nNo Relation found between {} and {}:".format(x,y))

r=Relations()
r.readCsv()
r.makeRelations()
r.findRelations('Sam','John')
r.findRelations('Jack','Peter')
r.findRelations('Alex','Joe')
r.findRelations('Joe','Peter') # Fails for this Output