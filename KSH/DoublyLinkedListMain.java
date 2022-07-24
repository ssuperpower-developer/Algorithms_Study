package AlgorithmStudy;

class Node<E> {
    Node() {
    }

    Node(E data) {
        this.data = data;
    }

    E data;
    Node<E> next = null;
    Node<E> prev = null;
}

class DoublyLinkedList<E> {
    private Node<E> firstNode;
    private Node<E> tailNode;
    private int size;

    DoublyLinkedList() {
        this.firstNode = null;
        this.tailNode = null;
        this.size = 0;
    }

    void add(E data) {
        if (firstNode == null) {
            firstNode = tailNode = new Node<E>(data);
            firstNode.next = firstNode;
            firstNode.prev = firstNode;
            size += 1;
        } else {
            tailNode.next = new Node<E>(data);
            tailNode.next.prev = tailNode;
            tailNode = tailNode.next;
            tailNode.next = firstNode;
            firstNode.prev = tailNode;
            size++;
        }
    }

    boolean remove(Object o) {
        Node<E> findNode = firstNode;

        if (isEmpty()) {
            return false;
        }

        for (int i = 0; i < size; i++, findNode = findNode.next) {
            if (o.equals(findNode.data)) {
                break;
            }
        }

        if (findNode.next == firstNode) {
            findNode.data = null;
            findNode.next = null;
            findNode.prev = null;
            size--;
            return true;
        } else {
            if (findNode == firstNode) {
                findNode.prev.next = findNode.next;
                findNode.next.prev = findNode.prev;
                firstNode = findNode.next;
                findNode.data = null;
                findNode.next = null;
                findNode.prev = null;
                size--;
                return true;
            }
            findNode.prev.next = findNode.next;
            findNode.next.prev = findNode.prev;
            findNode.data = null;
            findNode.next = null;
            findNode.prev = null;
            size--;
            return true;
        }
    }

    boolean contains(Object value) {
        return indexOf(value) >= 0;
    }

    int size() {
        return size;
    }

    Node<E> search(int index) {
        if (index > size / 2) {
            Node<E> x = tailNode;
            for (int i = size - 1; i > index; i--) {
                x = x.prev;
            }
            return x;
        } else {
            Node<E> x = firstNode;
            for (int i = 0; i < index; i++) {
                x = x.next;
            }
            return x;
        }
    }

    E get(int index) {
        return search(index).data;
    }

    E set(int index, E elements) {
        Node<E> replaceNode = search(index);
        replaceNode.data = elements;
        return elements;
    }

    boolean isEmpty() {
        return size == 0;
    }

    int indexOf(Object o) {
        if (!isEmpty()) {
            int index = 0;
            for (Node<E> findNode = firstNode; findNode.next != firstNode; findNode = findNode.next) {
                if (o.equals(findNode.data)) {
                    return index;
                }
                index++;
            }
            return index;
        }
        return -1;
    }

    void clear() {
        for (Node<E> x = firstNode; x != null;) {
            Node<E> nextNode = x.next;
            x.data = null;
            x.next = null;
            x.prev = null;
            x = nextNode;
        }
        firstNode = null;
        tailNode = null;
        size = 0;
    }

    void show() {
        if (isEmpty()) {
            System.out.println("empty");
        } else {
            Node<E> curNode = firstNode;
            do {
                System.out.println(curNode.data);
                curNode = curNode.next;
            } while (curNode != firstNode);
        }
    }
}

public class DoublyLinkedListMain {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.add(4);
        dll.add(3);
        dll.remove(4);
        dll.add(10);
        dll.add(13);
        System.out.println(dll.size());
        System.out.println(dll.indexOf(3));
        System.out.println(dll.contains(3));
        dll.show();
        System.out.println(dll.get(2));
        dll.set(2, 9);
        System.out.println(dll.get(2));
        dll.clear();
        dll.show();
    }
}
