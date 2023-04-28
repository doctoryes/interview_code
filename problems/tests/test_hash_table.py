
import hash_table

def test_hash_table_single_add():
    x = hash_table.HashMap()
    x['a'] = 1
    assert(str(x) == "{'a': 1}")

def test_hash_table_single_update():
    x = hash_table.HashMap()
    x['a'] = 1
    assert(str(x) == "{'a': 1}")
    x['a'] = 99
    assert(str(x) == "{'a': 99}")

def test_hash_table_multiple_add():
    x = hash_table.HashMap()
    x['a'] = 1
    x['b'] = 'blue'
    x['z'] = 5.67
    assert(str(x) == "{'a': 1, 'b': 'blue', 'z': 5.67}")

def test_hash_table_single_add_get():
    x = hash_table.HashMap()
    x['a'] = 1
    assert(x['a'] == 1)


