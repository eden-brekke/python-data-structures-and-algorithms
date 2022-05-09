# Challenge Summary
<!-- Description of the challenge -->
Write  a method in the existing binary tree module
that will traverse the tree and
return the maximum value within the tree

## Whiteboard Process
<!-- Embedded whiteboard image -->
I hope you can read this okay.
I wanted to give actual writing out of the whiteboard a shot
Let me know if I need to clarify or update this.
![whiteboard](CodeChallenge16.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
BigO for time and space should both be O(N)
where N is the number of nodes in the tree

I took the approach of recursion with a method within my method
where that method walks through the tree and compares an existing "max" to the value of each node
Then changes the "max" if the value within the node is larger

## Solution
<!-- Show how to run your code, and examples of it in action -->
My code works by passing two values into a walk method,
the root and a max that is an int that starts at 0
It will recursively walk through the left until it returns None and
then walk through the right until it returns none
Then it will return it's last value set to max
which should be the overall max of the tree
[Code Solutions](../../data_structures/binary_tree.py)
