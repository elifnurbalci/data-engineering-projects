# Higher Order Functions

## Every

<div align="left">

Write a function called every that takes a list and a predicate function. A predicate function is one that returns either True or False.

The every function should invoke the predicate function once for each element in the list. Each time it is invoked, the current element of the list should be passed as an argument to the predicate.

If the predicate function returns True for all elements of the list ,then the every function should return True. Otherwise, it should return False
</div>


## Some

<div align="left">

Write a function called some that takes a list and a predicate function as its arguments.

The some function should invoke the predicate function once for each element in the list. Each time it is invoked, the current element of the list should be passed as an argument to the predicate.

If the predicate function returns True for at least one element, the some function should return True. Otherwise, it should return False.
</div>

## Find

<div align="left">

Write a function called find that takes a list and a predicate function as its arguments.

It should return the first element that satisfies the given predicate function.
</div>

## Reimplementation: Map

<div align="left">

Reimplement the function, map. This function should take as its arguments:

A function, which will be invoked with each element in turn and return a new value.
A collection, which the function can map over.
You should use this resource for map to inform the behaviours you should test for and implement. Your function should do everything that the built-in map does, except the built-in map returns an iterator. You do not need to return an iterator, you should return the same data type as the collection that is passed in.

In your case, you should just design the map function to accept lists, sets or tuples.

Include testing to ensure that your passed function is invoked correctly and with the correct arguments.
</div>

## Reimplementation: Filter

<div align="left">

Reimplement the function, filter. This function should take as its arguments:

A function, which will be invoked with each element in turn and return a boolean.
A collection, which the function can map over
You should use this resource for filter to inform the behaviours you should test for and implement. Your function should do everything that the original filter does, except the original filter returns an iterator. You do not need to return an iterator, you should return the same data type as the collection that is passed in.

In your case, you should just design the filter function to accept lists, sets or tuples.

Include testing to ensure that your passed function is invoked correctly and with the correct arguments.
</div>

## For Each

<div align="left">

Write a function called for_each that takes a list and a function as arguments. The passed function should be invoked once for each of the elements in the given list.
</div>

## Reject

<div align="left">

Write a function called reject that takes a collection and a predicate function.

The reject function behaves in a similar way to the filter function you just re-implemented. However, the reject function should return a list of the elements of the collection that the predicate returns False for.
</div>

## Partition

<div align="left">

Write a function called partition that takes a collection and a predicate function.

The partition function will divide the elements of a given collection into two lists which will be nested within another list. This first list will contain the elements that the predicate returns True for, and the second list will contain the elements that the predicate returns False for. The predicate is invoked with each element in turn.
</div>

## Reduce Right

<div align="left">

Create a reduce_right function which take a list and a reducer function.

A reducer function is a function that takes two values and reduces it down to one.

The reduce_right function should invoke the passed function for every element starting with the first element on the right.
</div>

## Advanced Section - Sorted

<div align="left">

Reimplement the Python function, sorted. This function should take the following as its arguments:

A collection.
An optional argument key which specifies a function to use for sorting. The function should return a number that is then used for comparison.
It should also accept an optional argument reverse, this should default to be False. However, if it is True, then the order should be reversed.
</div>