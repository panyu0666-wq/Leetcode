class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next
class LinkedList:
    # 初始化
    def __init__(self):
        # 创建一个头结点
        self.dummy_head = ListNode()
        self.size = 0
        
    # 在链表的第一个元素之前添加一个新节点
    def addAtHead(self,val):
        self.dummy_head.next = ListNode(val=val,next=self.dummy_head.next)
        self.size += 1
        
    # 在链表的最后一个元素之后添加一个新节点
    def addAtTail(self,val):
        curr = self.dummy_head.next
        for _ in range(self.size):
            curr = curr.next
        curr.next = ListNode(val=val,next=curr.next)
        self.size += 1
    
    # 获取第index位置的元素
    def get(self,index):
        if index < 0 or index >= self.size:
            return -1 
        
        current = self.dummy_head.next
        for _ in range(index):
            current = current.next
        
        return current.val
    
    # 在第index位置上插入元素
    def addAtIndex(self,index,val):
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        
        for _ in range(index):
            current = current.next
        current.next = ListNode(val=val,next=current.next)
        self.size+=1
        
    # 删除index位置上的元素
    def deleteAtIndex(self,index):
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head
        
        for _ in range(index):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1