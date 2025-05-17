import ctypes 

class CustomList:
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize(self,new_Capacity):
        new_array = self.__create_array(new_Capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_Capacity

    def append(self,item):
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)

        self.array[self.size] = item
        self.size+=1
    
    def pop(self):
        if(self.size == 0):
            return 'Empty List , pop from empty list'
        
        popped_item = self.array[self.size-1]
        self.size = self.size - 1
        return popped_item

    def __len__(self):
        return self.size
    
    def __str__(self):
        output = ''
        for i in range(self.size):
            output = output + str(self.array[i]) + ','
        return '['+output[:-1]+']'
    
    def __getitem__(self,index):
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            return f"Index Error : Cannot find any element at index {index}"

    def insert(self,pos,element):
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)

        for i in range(self.size,pos,-1):
            self.array[i] = self.array[i-1]
        
        self.array[pos] = element

        self.size += 1 

    def remove(self,value):
        found = False
        for i in range(self.size):
            if self.array[i] == value:
                found = True
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                break
        if not found:
            print("Value Error: Value not found in list")

    def delete(self,index):
        if index < 0 or index >= self.size:
            print("Index Error: Cannot remove, index out of bounds")
            return
        
        for i in range(index,self.size-1):
            self.array[i] = self.array[i+1]

        self.size -=1


    def clear(self):
        self.size=0

myList = CustomList()
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)

print(myList)
# print(myList[2])

# myList.delete(4)

myList.remove(30)

print("deleted",myList)