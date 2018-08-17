class Difference:
    def __init__(self, a):
        self.__elements = a
# Add your code here
    def computeDifference(self):
        el=self.__elements
        store=[]
        for i in range(0,len(el)):
            for j in range(0,len(el)):
                store.append(abs(el[i]-el[j]))
        self.maximumDifference = max(store)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)