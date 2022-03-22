from itertools import permutations

class Solution():
    def __int__(self,List):
        self.List = List

    def __len__ (self):
        return len(self.List)

    def solution1(self,List):
        n = len(List)
        LL = list(permutations(List,n))
        return LL
    
    def solution2(self,Listd,List,temp=list(),LL=list()):
        n = len(Listd)
    
        for i in List:
            List2 = List.copy();temp2 = temp.copy()
            temp2.append(i)
            List2.remove(i)

            if len(temp2) == n:
                LL.append(temp2)
            else:
                Solution.solution2(self,Listd,List2,temp2,LL)

        return LL


if __name__ == '__main__':
    Result = Solution()
    A = [1,2,3,4] #input
    print (*Result.solution1(A))
    print (*Result.solution2(A,A))




'''
    def solution2(self,Listd,List,temp=list(),LL=list()):
        n = len(Listd)
    
        for i in List:
            List2 = List.copy()
            temp2 = temp.copy()
            temp2.append(i)
            List2.remove(i)
#            for j in List2:
#                List3 = List2.copy()
#                temp1 = temp.copy()
#                temp1.append(j)
#                List3.remove(j)
#                for k in List3:
#                    List4 = List3.copy()
#                    temp2 = temp1.copy()
#                    temp2.append(k)
#                    List4.remove(k)
            print (temp,len(temp2))
            if len(temp2) == n:
                LL.append(temp2)
            else:
                Solution.solution2(self,Listd,List2,temp2,LL)
'''
