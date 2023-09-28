class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    head=Node(None) 

    #헤더부터 탐색해 뒤에 새로운 노드 추가
    def append(self, data):
        cur = self.head
    
        while cur.next is not None:
            cur=cur.next
        cur.next = Node(data)


    #모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not Node:
            print(cur.data)
            cur = cur.next

    #노드 인덱스 알아내기
    def get_node(self, index):
        curNode = self.head
        cnt=0
        while cnt<index:
            cnt+=1
            curNode = curNode.next
        return curNode


    #삽입
    def add_node(self, index, value):
        new_Node = Node(value)
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node 
            return
        prev_node = self.get_node(index-1)
        next_node = prev_node.next
        prev_node.next = new_Node
        new_Node.next = next_node

    

    #삭제
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        pre_node = self.get_node(index-1)
        pre_node.next = pre_node.next.next
    
linked = LinkedList()
linked.append(1)
print(linked.get_node)
linked.append(3)
linked.append(10)
linked.add_node(2,2)
linked.delete_node(1)
linked.print_all()
