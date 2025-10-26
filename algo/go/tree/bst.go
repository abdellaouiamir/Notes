package main

import "fmt"

type node struct {
	val int
	leftNode *node
	rightNode *node
}

func (n *node)insert(val int) {
	if n.val == val {
		return
	} else if val < n.val {
		if n.leftNode == nil {
			n.leftNode = &node{val: val}
		} else {
			n.leftNode.insert(val)
		}
	} else if val > n.val {
		if n.rightNode == nil {
			n.rightNode = &node{val: val}
		} else {
			n.rightNode.insert(val)
		}
	}
}

func (n *node) delet(val int) *node {
	if n == nil {
		return nil
	}
	if val < n.val {
		if n.leftNode != nil {
			n.leftNode = n.leftNode.delet(val)
		}
	} else if val > n.val {
		if n.rightNode != nil {
			n.rightNode = n.rightNode.delet(val)
		}
	} else { // Node to be deleted found
		if n.leftNode == nil {
			return n.rightNode
		} else if n.rightNode == nil {
			return n.leftNode
		} else { // Node with two children
			successor := n.rightNode
			for successor.leftNode != nil {
				successor = successor.leftNode
			}
			n.val = successor.val
			n.rightNode = n.rightNode.delet(successor.val)
		}
	}
	return n
}

func (n *node)preorder() {
	if n != nil {
		fmt.Println(n.val)
		n.leftNode.preorder()
		n.rightNode.preorder()
	}
}

func (n *node)inorder() {
	if n != nil {
		n.leftNode.inorder()
		fmt.Println(n.val)
		n.rightNode.inorder()
	}
}

func (n *node)postorder() {
	if n != nil {
		n.leftNode.postorder()
		n.rightNode.postorder()
		fmt.Println(n.val)
	}
}

func main() {
	var bst = node{val: 8}
	bst.insert(8)
	bst.insert(2)
	bst.insert(9)
	bst.insert(4)
	bst.insert(12)
	bst.insert(93)
	bst.inorder()
	fmt.Println("delete")
	bst.delet(2)
	bst.delet(100)
	bst.inorder()
}

