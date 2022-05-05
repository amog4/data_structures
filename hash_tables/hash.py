class HashTable:

    def __init__(self,size):

        self.data_map = [None] * size

    def __hash(self,key):

        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        
        return my_hash

    def print_table(self):

        for i, v in self.data_map:
            print(f'{i} value {v}')


    def set_key(self,key,value):

        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    
    def get_items(self,key):

        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        
        return None

    



    