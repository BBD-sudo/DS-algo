class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_begin(108)
    ll.insert_at_begin(105)
    ll.insert_at_begin(56)
    ll.print()
