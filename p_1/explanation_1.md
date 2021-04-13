Since the problem requires dealing with the order in which values ​​are inserted into the cache object, the OrderedDict method is the best approach.

OrderedDict stores the order in which keys are inserted into the object. A regular dictionary does not take into account the order of insertion in the object, and iterating it provides the values ​​in any order.

The created solution has efficiency O (1), meeting the requirement of the problem and some edge use cases have also been covered.