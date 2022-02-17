# Udacity_Data_Structure_Nanodegree_Project_3
PROBLEM 1: 
In this problem, we have taken 2 integer values and identified them as ‘low’ and ‘high’. We consider original number to be old and the floored number of that to be new. We square the new number and compare it with the given input. Followed by which we use integer division operator to find the necessary output. 
Time Complexity: O(logn) 
Space Complexity: O(1)

PROBLEM 2: 
For this task, we will use divide and conquer method and keep splitting the list at every iteration. We can perform binary search on the split lists and find our required number.
Time Complexity: O(logn) 
Space Complexity: O(n)

PROBLEM 3: 
To maximize the sum of two elements from the array, we will traverse through the list and store the frequency of each number in a different array. Through this, we will create another array of 2 numbers. 
Time Complexity: O(logn) 
Space Complexity: O(1)

PROBLEM 4: In order to sort the list in single traversal, we will keep a hold on 0 and 2 and interchange their positions. 
Time complexity: O(n) 
Space Complexity: O(n)

PROBLEM 5: In this problem, we will store n number of words without taking extra memory for similar words and add suffixes recursively. 
Time Complexity of insert function: O(n) 
Time Complexity of find function: O(n) 
Time Complexity of split_path function: O(n) 
Space Complexity of insert function: O(n) 
Space Complexity of find function: O(n)

PROBLEM 6: For this problem, we traverse through the list using linear search. We create 2 variables holding max and min values and while traversing through the list, identify if any number is greater/smaller than them and accordingly update the values.
Time Complexity: O(n) 
Space Complexity: O(1)

PROBLEM 7: Using the same principles in problem 5, we solve the problem using Trie data structure and make three classes to perform the insert, find/lookup functions and traverse through the string without using any extra memory. 
Time Complexity of insert function: O(n) 
Time Complexity of split_path function: O(n) 
Time Complexity of find function: O(n) 
The space complexity of insert function: O(n) 
The space complexity of find function: O(n)
