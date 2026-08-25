class queue:
    def __init__(self):
        self.f=-1
        self.r=-1
        self.q=[0]*5 # this is the length of the index matlab it will have 4 elements


    def insert(self,y):
        if self.r==4:

         print("queue is overflow")
         return
        
        self.r=self.r+1

        self.q[self.r]=y

        if self.f==-1:
         self.f=0

    def delete(self,x):
        if self.f==-1:
          print("the queue is empty")
          return
        x=self.q[self.f]
        if self.f ==self.r:
          self.f=self.r=-1
        else:
            self.f+=1
            print("eleemnt removed" , x)
            return x
        
    def display(self):
        if self.f== -1:
            print("queue is underflow")   
    
    
        else:
            print("queue elements are:")
            for i in range(self.f, self.r + 1):
             print(self.q[i])
            print()
          
q = queue()

while True:
   
    ch = int(input("\n1. insert  \n2. delete \n3. display \n4. Exit \n Exit your choice" ))

    if ch ==1:
      x=int(input("enter element:"))
      q.insert(x)
    elif ch==2:
      q.delete()

    elif ch ==3:
       q.display()

    elif ch==4:
       break

    else:
       print("invalid choice madam")
        