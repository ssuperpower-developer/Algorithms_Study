#include <iostream>

using namespace std;

struct Node
{
    int studentNumber;
    int studentScore;
    Node *left;
    Node *right;

public:
    Node(int studentNumber, int studentScore = 0)
    {
        this->studentNumber = studentNumber;
        this->studentScore = studentScore;
        left = NULL;
        right = NULL;
    }
};

class BinaryTree
{
private:
    Node *headNode;

public:
    BinaryTree()
    {
        headNode = NULL;
    }
    ~BinaryTree();

    void AddNode(int a, int b);
    // bool GetData(Node *node, int &data);
    void PreorderPrint();
    void PreorderPrint(Node *node);
    // void RemoveNode();
};
