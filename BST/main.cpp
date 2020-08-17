//
//  main.cpp
//  BST
//
//  Created by Sam lindaman on 8/16/20.
//  Copyright © 2020 Sam lindaman. All rights reserved.
//

#include <iostream>
using namespace std;
  
class BST
{
    int data;
    BST *leftNode, *rightNode;
  
    public:
    BST();
    BST(int);

    BST* Insert(BST *, int);
    void inOrder(BST *);
    void postOrder(BST *);
    void preOrder(BST *);
};
  
// Default Constructor
BST :: BST() : data(0), leftNode(NULL), rightNode(NULL){}
  
// Constructor with Parameter
BST :: BST(int value)
{
    data = value;
    leftNode = rightNode = NULL;
}
  
// Insert definition.
BST* BST :: Insert(BST *root, int value)
{
    if(root == NULL)
    {
        return new BST(value);
    }
    
    // does not allow for repeat data
    if (root->data == value){
        return root;
    }
    
    // Insert data.
    if(value > root->data)
    {
        root->rightNode = Insert(root->rightNode, value);
    }
    else
    {
        root->leftNode = Insert(root->leftNode, value);
    }
      
    return root;
}
  
// Inorder traversal function.
void BST :: inOrder(BST *root)
{
    if(root == NULL)
    {
        return;
    }
    inOrder(root->leftNode);
    cout << root->data << " ";
    inOrder(root->rightNode);
}

// Post order traversal
void BST:: postOrder(BST *root){
    if (root == NULL) {
        return;
    }
    postOrder(root->leftNode);
    postOrder(root->rightNode);
    cout<< root->data<<" ";
    
}

// Pre order traversal
void BST:: preOrder(BST *root){
    if (root == NULL) {
        return;
    }
    cout<< root->data<<" ";
    postOrder(root->leftNode);
    postOrder(root->rightNode);
    
}

  
int main()
{
    int array[] = {45,67,77,43,1,0,9,33,99,87,45,45,45,47,68,100};
    
    BST tree, *root = NULL;
    
    root = tree.Insert(root, 55);
    
    for(int i = 0;i<*(&array+1)-array;i++){
        tree.Insert(root, array[i]);
    }
  
    cout<<"In Order: "<<endl;
    tree.inOrder(root);
    cout<<endl<<endl;
    cout<<"Post Order:"<<endl;
    tree.postOrder(root);
    cout<<endl<<endl;
    cout<<"Pre Order:"<<endl;
    tree.preOrder(root);
    cout<<endl<<endl;
    
    
    return 0;
}
