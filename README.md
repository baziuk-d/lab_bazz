# Рівень 1
## Варіант 2
Існує три найпоширеніші способи проходження бінарних дерев вглиб: прямий (pre-order), зворотній (post-order) та серединний (in-order).

Реалізуйте функцію, яка отримує на вхід вершину бінарного дерева та виконує його зворотній обхід (Post-order traversal) та повертає значення вузлів у списку у відповідному порядку.

Розглянемо таке бінарне дерево:

    1
   / \
  2    3
   \  / \
   5  6  7
Під час прямого обходу це дерево буде відвідане в такому порядку: [5, 2, 6, 7, 3, 1]

Функція post_order_traversal(root: BinaryTree) -> List отримує на вхід корінь бінарного дерева, який має наступний вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
