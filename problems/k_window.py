"""
A K-window is defined to be all the unique elements in the first K elements of a list.

Given a list1, list2, and value K:

Remove the minimum number of elements required to make the K-windows
of list1 and list2 have no elements in common.
"""

def _build_elem_dict(list, k):
    """
    Traverses k elements in the list and builds a dictionary specifying
    elements as keys and a list of element indices as values.
    For example,
    [1, 1, 2, 4, 4]
    would return:
    {1 : [0, 1], 2 : [1], 4 : [3, 4]}
    """
    list_elems = {}
    for idx, e in enumerate(list):
        if idx >= k:
            break
        if e in list_elems:
            list_elems[e].append(idx)
        else:
            list_elems[e] = [idx]
    return list_elems


def _remove_items(list, idxs):
    """
    Remove the list elements specified by the indices in reverse sorted index order.
    This order is used to keep all indices valid after each element removal.
    """
    idxs = sorted(idxs)
    idxs.reverse()
    for idx in idxs:
        del list[idx]

def unique_k_window(list1, list2, k):
    num_removals = 0
    while True:
        list1_removals = []
        list2_removals = []
        list1_elems = _build_elem_dict(list1, k)
        list2_elems = _build_elem_dict(list2, k)
        for elem, idxs in list1_elems.items():
            if elem in list2_elems:
                # Common element in the K-window.
                # Determine from which list to remove the element.
                # Always remove the minimal number of elements.
                if len(idxs) < len(list2_elems[elem]):
                    # Remove the element from list1.
                    list1_removals.extend(idxs)
                else:
                    # Remove the element from list2.
                    list2_removals.extend(list2_elems[elem])

        if len(list1_removals) == 0 and len(list2_removals) == 0:
            # No more removals to perform.
            break

        # Remove the elements.
        _remove_items(list1, list1_removals)
        _remove_items(list2, list2_removals)
        num_removals += len(list1_removals) + len(list2_removals)

    return num_removals

