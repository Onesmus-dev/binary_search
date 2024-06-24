class BinarySearchTreeNode:
    #instantiates our binary class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            #add the val in the left subtree
            if self.left:
                #so now this adds a child to the left node by recursively calling the add_child function
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    #in_order Traversal
    def in_order_traversal(self):
        elements = []
        #visit left
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        
        return elements
    def search(self,val):
        if self.data == val:
            return True
        if val <self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    #recursively
    def find_max_recursive(self):
        if not self.right: #checks if there is a child to the right
            return self.data#if not returns the value 
        else:
            return self.right.find_max_recursive()
        
        #using the While loop 
    def find_max(self):
        #traves the tree
        #goes to the right gets the biggest value
        current = self
        while current.right:
            current = current.right
        return current.data
    #we are doing jus as the max 
    # since all left values are less than root we move to the lowest and less value on the left  
    def find_min(self):
        current = self #this acts a pointer
        while current.left:#we make sure that we loop through the left nodes.

            current = current.left #updates the value of current 

        return current.data #returns the final lowest left value 
    
    #let us do the sum of elements in the list
    #we already have the the in_order traverse
    #my thinking is we can get the function and add the values.
    
    def calculate_sum(data):
        sum = 0 #this tries to make the sum my starting point for summation.
        elements = numbers_tree.in_order_traversal()
        for i in elements:
            sum +=i
        return sum
    
    #Delete function

    def delete(self, val):
        if val <self.data:#checks if the val is on the left side of the tree
            if self.left:
                self.left.delete(val) #this recursively calls the delete function till the val = data 
            else:
                return "The value is not in the tree" #if there is no left nodes of the tree then it returns the msg
        elif val > self.data:
            if self.right:
                self.right =self.right.delete(val)
            else:
                return "The value is not in the tree" # you can ignore this else return since in python it would return None
            
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right  is None:
                return None
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right= self.right.delete(min_val)
        return self
        
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4,1,20,23,18,34,56,3,10]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.calculate_sum())
    numbers_tree.delete(10)
    print("After deleting 10", numbers_tree.in_order_traversal())