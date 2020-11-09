# sudoku_solver
To solve various Sudoku problems in the Python language.


## Version 0.1:
A Finnish mathematician claims to have designed the world's most difficult Sudoku, which has a _**unique**_ solution:
 
![alt text](https://abcnews.go.com/images/US/ht_level_11_sudoku_jef_120629_wblog.jpg?raw=true).

See https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku for more details. 

As is shown in the above picture, to solve a sudoku, we need to assign digits from the set {1,2,...,9} to the empty cells of the 9*9 grid so that every row, column, and subgrid contains exactly one of the digits from 1 to 9. Traditionally, such a problem can be solved by a back-tracking method, which is a depth-fist search (brute force) algorithm, as it will completely explore if one branch extends to a possible solution before moving to another branch. In this part, we solve the above Sudoku, with a slightly more refined version of back-tracking method, that is, at each recursive step, we choose the key with the least amount of possible values and guess from the values of this key in a numerical manner so that our chances of making a "good" guess is optimal. 
