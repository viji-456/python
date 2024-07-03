class student:
    def __init__ (self,name,reg,m1,m2,m3):
        self.name=name
        self.reg=reg
        self.m1=m1
        self.m2=m2
        self.m3=m3
        def avg(self):
            a=int((m1+m2+m3)/3)
            avg[name]=a
        def rank(self):
            i=0
            rank=1
            temp=()
            while i<n:
                print()
                keymax=max(zip(avg.value(),avg.keys()))
                print("Rank=",rank,end="")
                print("(Average marks and name)=",keymax)
                a=keymax[1]
                del avg[a]
                rank +=1
                i+=1
n=int(input("enter no. of students:"))
stud={}
avg={}
m=[]
for i in range(n):
    name=input("Enter a name:")
    reg=input("Enter a reg no:")
    m1=int(input("Enter marks1:"))
    m2 = int(input("Enter marks2:"))
    m3 = int(input("Enter marks3:"))
    st=student(name,reg,m1,m2,m3)
    stud[reg]=st
    st.avg()
st.rank()
