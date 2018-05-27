from hr.llists import graph

def test_empty_has_no_cycles():
    assert not graph.has_cycle(None)

def test_empty_has_no_cycles_single_node():
    a = graph.Node()
    assert not graph.has_cycle(a)

def test_no_cycles_simple():
    b = graph.Node()
    a = graph.Node(next_node=b)
    assert not graph.has_cycle(a)

def test_single_node_cycle():
    a = graph.Node()
    a.next = a
    assert graph.has_cycle(a)

def test_simple_has_cycle():
    b = graph.Node()
    a = graph.Node(next_node = b)
    b.next = a
    assert graph.has_cycle(a)

def test_simple_has_cycle_start_off_1():
    d = graph.Node()
    c = graph.Node(next_node = d)
    b = graph.Node(next_node = c)
    d.next = b
    a = graph.Node(next_node = b)
    assert graph.has_cycle(a)

def test_simple_has_cycle_start_off_2():
    e = graph.Node()
    d = graph.Node(next_node = e)
    c = graph.Node(next_node = d)
    b = graph.Node(next_node = c)
    e.next = b
    a = graph.Node(next_node = b)
    assert graph.has_cycle(a)
