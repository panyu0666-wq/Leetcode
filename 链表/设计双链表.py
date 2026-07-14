class ListNode:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def addAtHead(self,val):
        new_node = ListNode(val,None,self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size+=1 
    def addAtTail(self,val):
        new_node = ListNode(val,self.tail,None)
        if self.tail:
            self.tail = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size+=1 
        
    def addAtIndex(self,index,val):
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            # 减少访问次数
            if index < self.size // 2:
                current = self.head
                for i in range(index-1):
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size-index):
                    current = current.prev
                new_node = ListNode(val,current,current.next)
                current.next.prev = new_node
                current.next = new_node
                self.size+=1
        def get(self,index):
            if index < 0 or index >= self.size:
                return -1
            if index < self.size//2:
                current = self.head
                for i in range(index):
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size-index-1):
                    current = current.prev
            return current.val
        def deleteIndex(self,index):
            if index < 0 or index >= self.size:
                return -1
            if index == 0:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            elif index == self.size - 1:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
                else:
                    self.head = None
            else:
                if index < self.size // 2:
                    current = self.head
                    for i in range(index):
                        current = current.next
                else:
                    current = self.tail
                    for i in range(self.size - index - 1):
                        current = current.prev
                current.prev.next = current.next
                current.next.prev = current.prev
            self.size -= 1

                    