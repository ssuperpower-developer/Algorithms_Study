#include <iostream>
#include "BinaryTree.h"

int main()
{
    BinaryTree *tree = new BinaryTree();

    tree->AddNode(20191234, 100);
    tree->AddNode(20211234, 90);
    tree->AddNode(20194321, 96);
    tree->PreorderPrint();
}