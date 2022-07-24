#include <iostream>
#include "BinaryTree.h"

using namespace std;

void BinaryTree::AddNode(int studentNumber, int studentScore)
{
    Node *tmpNode;
    Node *newNode = new Node(studentNumber, studentScore);
    if (headNode == NULL)
    {
        headNode = newNode;
    }
    else
    {
        Node *currNode = headNode;
        while (currNode != nullptr)
        {
            tmpNode = currNode;
            if (newNode->studentNumber < currNode->studentNumber)
            {
                currNode = currNode->left;
            }
            else
            {
                currNode = currNode->right;
            }
        }
        if (newNode->studentNumber < tmpNode->studentNumber)
        {
            tmpNode->left = newNode;
        }
        else
        {
            tmpNode->right = newNode;
        }
    }
}

// bool BinaryTree::GetData(Node *node, int &data)
// {
//     if (node == NULL)
//     {
//         return false;
//     }

//     cout << "GetData : " << data << endl;
//     return true;
// }

void BinaryTree::PreorderPrint()
{
    PreorderPrint(headNode);
}

void BinaryTree::PreorderPrint(Node *node)
{
    if (node == nullptr)
    {
        return;
    }
    cout << node->studentNumber << " : " << node->studentScore << endl;
    PreorderPrint(node->left);
    PreorderPrint(node->right);
}

// void BinaryTree::RemoveNode()
// {
// }
