# Python3 program to demonstrate  
# List  
def testlist():
    # Creating a List 
    List = [] 
    print("Blank List: ") 
    print(List) 
    
    # Creating a List of numbers 
    List = [10, 20, 14] 
    print("\nList of numbers: ") 
    print(List) 
    
    # Creating a List of strings and accessing 
    # using index 
    List = ["Geeks", "For", "Geeks"] 
    print("\nList Items: ") 
    print(List[0])
    print(List[1])    
    print(List[2])
    FruitList = ["Orange", "Grapes", "apple"] 
    FruitList.append("cherry")
    FruitList.insert(1,"kiwi")
    FruitList.remove("kiwi")
    FruitList.pop(2)
    #loop
    for x in FruitList:
        print(x)
    #loop
    for i in range(len(FruitList)):
        print(FruitList[i])
    
    #Loop
    [print(x) for x in FruitList]


    print(FruitList)



def testtuple():

    # Creating an empty Tuple 
    Tuple1 = () 
    print("Initial empty Tuple: ") 
    print (Tuple1) 
    
    # Creating a Tuple with 
    # the use of list 
    list1 = [1, 2, 4, 5, 6] 
    print("\nTuple using List: ") 
    print(tuple(list1)) 
    
    #Creating a Tuple  
    #with the use of built-in function 
    Tuple1 = tuple('Geeks') 
    print("\nTuple with the use of function: ") 
    print(Tuple1)

def testset():
    # Creating a Set 
    set1 = set() 
    print("Intial blank Set: ") 
    print(set1) 
    
    # Creating a Set with 
    # the use of Constructor 
    # (Using object to Store String) 
    String = 'GeeksForGeeks'
    set1 = set(String) 
    print("\nSet with the use of an Object: " ) 
    print(set1) 
    
    # Creating a Set with 
    # the use of a List 
    set1 = set(["Geeks", "For", "Geeks"]) 
    print("\nSet with the use of List: ") 
    print(set1)

if __name__ == '__main__':
    #List is a collection which is ordered and changeable. Allows duplicate members.
    testlist()
    #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    #testtuple()
    #Set is a collection which is unordered and unindexed. No duplicate members.
    #testset()
    #Dictionary is a collection which is unordered and changeable. No duplicate members.
