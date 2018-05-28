from hr.graphs.trees import Node, checkBST


def test_single_node_bst():
    assert checkBST(Node(0))


def test_check_bst_1():
    assert checkBST(Node(4, Node(2), Node(6)))


def test_check_bst_2():
    assert checkBST(Node(4, Node(2, Node(1)), Node(6)))


def test_check_bst_3():
    assert checkBST(Node(4, Node(2, Node(1)), Node(6, None, Node(7))))


def test_check_bst_4():
    assert not checkBST(Node(4, Node(2, Node(1)), Node(6, None, Node(5))))


def test_check_bst_5():
    assert not checkBST(Node(4, Node(9, Node(1)), Node(6, None, Node(7))))
