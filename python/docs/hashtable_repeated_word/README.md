# Hashtable repeated word

### Challenge Summary
Create a function called repeated word that finds the first word to occur more than once in a string.

### Collaboration
Got help with this from Roger. :) 

### Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard](Codechallenge31.png)

### Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time/Space: O(N) where N is the number of words in the string

### Solution
<!-- Show how to run your code, and examples of it in action -->

* Create a function that accepts a string
* Search through the string for words
* Create an Empty set
* Check each word: if in set?
  * no? Add to set!
  * yes? That's a repeat! return word!

[Code Solution](../../code_challenges/hashtable_repeated_word.py)
