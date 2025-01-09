def ft_filter(func, iterable_object):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if func is None:
        for inner_obj in iterable_object:
            if inner_obj:
                yield inner_obj
    else:
        for inner_obj in iterable_object:
            if func(inner_obj):
                yield inner_obj
