Since the problem requires dealing with the order in which values ​​are inserted into the cache object, the OrderedDict method is the best approach.

OrderedDict stores the order in which keys are inserted into the object. A regular dictionary does not take into account the order of insertion in the object, and iterating it provides the values ​​in any order.

The created solution has time efficiency O(1) and space efficiency O(1) for both get and set methods.