#assignment1_part1

class ListDivideExeption(Exception):
        pass
def listDivide(number,divide=2):#1 
        ans=0 #initialize ans

        try:
                for x in number:#looking for numbers in list number
                        if x % divide==0:
                                ans=ans+1
        except:
                raise MyException()
        print ans
        return ans
def testListDivide():
        
        try:
                listDivide([1,2,3,4,5])
                listDivide([2,4,6,8,10])
                listDivide([30, 54, 63,98, 100], divide=10)
                listDivide([])
                listDivide([1,2,3,4,5], 2)
        except TyperError:
                raise ListDivideExeption
testListDivide()# call fucntion
        

                
                        
