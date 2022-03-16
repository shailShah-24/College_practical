# 20CE134 Shail shah
#Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

class stack:
    def __init__(self):  # create the constructor
        self.arr = []

    def push(self, data):  # using push method you can add the element in stack
        self.arr.append(data)

    def pop(self):  # using pop methi\od you can delete the top most element in stack
        return self.arr.pop()

    def is_empty(self):  # check if stack is empty or not
        return self.arr == []

    def display(self):  # traversal method
        if (self.is_empty()):  # first check if stack is empty or not
            print("No element in stack")
        for i in self.arr:
            print(i, end=" ")
        print("\n")


st = stack()  # create the object

st.push(1)  # push the element 1
st.push(2)  # push the element 2
st.push(3)  # push the element 3
print("Number of  element in stack")
st.display()  # display 1 2 3
st.pop()  # pop the element its pop top most element 3
print("Number of element in stack")
st.display()  # display 1 2