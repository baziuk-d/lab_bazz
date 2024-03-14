import unittest
from code_lab_3 import BinaryTree, post_order


class TestPostOrderTraversal(unittest.TestCase):
    def test_post_order_traversal(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        self.assertEqual(post_order(root), [9, 20, 3])


if __name__ == '__main__':
    unittest.main()