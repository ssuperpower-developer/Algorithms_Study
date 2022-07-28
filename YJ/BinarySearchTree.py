class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.rootNode = None
        

    def insert(self, data):
        if self.rootNode is None:
            self.rootNode = Node(data)
        else:
            self.base = self.rootNode
            while True:
                if data == self.base.data:
                    print("중복된 데이터 입니다.")
                    break
                elif data > self.base.data:
                    if self.base.right is None:
                        self.base.right = Node(data)
                        break
                    else:
                        self.base = self.base.right
                else:
                    if self.base.left is None:
                        self.base.left = Node(data)
                        break
                    else:
                        self.base = self.base.left

    def remove(self, data):
        self.searched = False
        self.cur_node = self.rootNode
        self.parent = self.rootNode
        while self.cur_node:
            if self.cur_node.data == data:
                self.searched = True
                break
            elif self.cur_node.data > data:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right
        if self.searched:#지울거 찾음
            # rootNode를 지우는 경우
            if self.cur_node.data == self.parent.data:
                self.rootNode = None #None 처리하면 데이터는 삭제됨!
            else: #rootNode가 아닌 그외의 경우
                # 1) 삭제하는 node가 leaf node인 경우
                if self.cur_node.left is None and self.cur_node.right is None:
                    if self.parent.data > self.cur_node.data:
                        self.parent.left = None
                    else:
                        self.parent.right = None

                # 2) 삭제하는 node의 자식이 하나인 경우
                elif self.cur_node.left is not None and self.cur_node.right is None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.left
                    else:
                        self.parent.right = self.cur_node.left
                elif self.cur_node.left is None and self.cur_node.right is not None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.right
                    else:
                        self.parent.right = self.cur_node.right

                # 3) 삭제하는 node의 자식이 둘인 경우
                elif self.cur_node.left is not None and self.cur_node.right is not None:
                    self.tmp_parent = self.cur_node.right
                    self.tmp_cur = self.cur_node.right
                    while self.tmp_cur.left:
                        self.tmp_parent = self.tmp_cur
                        self.tmp_cur = self.tmp_cur.left
                    if self.tmp_cur.right is not None:
                        self.tmp_parent.left = self.tmp_cur.right
                    else:
                        self.tmp_parent.left = None
                    if self.parent.data > data:
                        self.parent.left = self.tmp_cur
                    else:
                        self.parent.right = self.tmp_cur
                    self.tmp_cur.left = self.cur_node.left
                    self.tmp_cur.right = self.cur_node.right
        else: #지울거 못 찾음
            print("해당 데이터가 존재하지 않습니다.")

    def search(self, data):
        self.base = self.rootNode
        while self.base:
            if self.base.data == data:
                return True
            elif self.base.data > data:
                self.base = self.base.left
            else:
                self.base = self.base.right
        return False


    #재귀함수를 쓰면 구현할 수 있음 
    #전위 순회
    def preOrder(self, node):
            if not node:
                return
            print(node.data, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    #중위 순회
    def inOrder(self, node):
            if not node:
                return
            self.inOrder(node.left)
            print(node.data, end=' ')
            self.inOrder(node.right)

    #후위 순회
    def PostOrder(self, node):
            if not node:
                return
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print(node.data, end=' ')

b = BinarySearchTree()
b.insert(31)
b.insert(15)
b.insert(41)
b.insert(12)
b.insert(18)
b.insert(40)
b.insert(51)
b.insert(11)
b.insert(13)
b.insert(16)
b.insert(19)
b.insert(17)
b.insert(20)

b.preOrder(b.rootNode)
print()
b.inOrder(b.rootNode)
print()
b.PostOrder(b.rootNode)