class UnorderedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        string = ''
        current = self.head
        while current != None:
            string += current.__str__()
            current = current.getNext()
        string += 'None'
        return string
            
    def isEmpty(self):
        return self.head == None