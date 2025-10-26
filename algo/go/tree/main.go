package main

import (
	"fmt"
)

type Node struct {
	val int
	right *Node
	left *Node
}
func (n *Node) insert(val int) {
	if val == n.val {
		return
	}
	if val < n.val {
		if n.left == nil {
			n.left = &Node{val: val}
		}else{
			n.left.insert(val)
		}
	}else if val > n.val {
		if n.right == nil {
			n.right = &Node{val: val}
		}else{
			n.right.insert(val)
		}
	}
}
func (n *Node) delete(val int) *Node {
	if n == nil {
		return nil
	}
	if val < n.val {
		if n.left == nil {
			return nil
		}
		n.left = n.left.delete(val)
	} else if val > n.val {
		if n.right == nil {
			return nil
		}
		n.right = n.right.delete(val)
	} else {
		if n.left == nil {
			return n.right
		} else if n.right == nil {
			return n.left
		} else {
			min_node := n.right
			for min_node.left != nil {
				min_node = min_node.left
			}
			n.val = min_node.val
			n.right.delete(min_node.val)
		}
	}
	return n
}
func (n *Node) delete2(val int) {
	if n == nil {
		return
	}
	if val < n.val {
		if n.left == nil {
			return
		}
		n.left.delete(val)
	} else if val > n.val {
		if n.right == nil {
			return
		}
		n.right.delete(val)
	} else {
		if n.left == nil {
			n = n.right
			return
		} else if n.right == nil {
			n = n.left
			return
		} else {
			min_node := n.right
			for min_node.left != nil {
				min_node = min_node.left
			}
			n.val = min_node.val
			n.right.delete(min_node.val)
		}
	}
}
func (n *Node) postNode() {
	fmt.Println(n.val)
	if n.left != nil {
		n.left.postNode()
	}
	if n.right != nil {
		n.right.postNode()
	}
}

func main() {
	var n *int
	var nn int = 7
	n = &nn
	nn = *n
	fmt.Println(n)
	var bt *Node
	bt = &Node{val: 5}
	bt.insert(10)
	bt.insert(2)
	bt.insert(2)
	bt.insert(3)
	//bt.insert(4)
	//bt.insert(9)
	//bt = bt.delete(3)
	bt.delete2(4)
	bt.delete2(3)
	bt.postNode()
}

type BinaryTree struct {
	root *Node
}

func (b BinaryTree) insert(val int) {
	if b.root == nil {
		b.root = &Node{val: val}
		return
	}
	var parent *Node
	current := b.root
	for current != nil {
		parent = current
		if val < current.val {
			current = current.left
		}else if val > current.val {
			current = current.right
		}else {
			return
		}
	}
	if val < parent.val {
		parent.left = &Node{val: val}
	} else if val > parent.val {
		parent.right = &Node{val: val}
	}
	return
}
