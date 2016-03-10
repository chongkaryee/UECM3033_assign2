UECM3033 Assignment #2 Report
========================================================

- Prepared by: Chong Kar Yee
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

https://github.com/chongkaryee/UECM3033_assign2.git

Explain your selection criteria here.
A sparse matrix is a matrix in which most of the elements are zero in numerical analysis. If the matrix is sparse matrix, we will use SOR method.  condition = np.count_nonzero(A) > 1/2 *len(A). If the nonzero element in matrix A is more than half of total elements in matrix A, it will carry out LU factorization, Conversely, if the nonzero element in matrix A is less than half of total elements in matrix A, then it will perform SOR method. Therefore, sparse matrix is better to solve by using SOR method. 

Explain how you implement your `task1.py` here.
There are 3 self-defined function in task1.py that is lu, sor and solve function. In lu function, matrix A was decomposed into LU form which is lower matrix form and upper matrix form. In sor function, we need a parameter called omega. If a matrix is symmetric and positive definite, omega can set to be in the range of (1 < omega < 2) that will converge for any initial vector. If 0 < omega <1, SOR method will have a little convergence but if omega is greater than 2 , SOR method will diverge. After the system matrix has been test by the condition, then it will solve by using np.linalg.solve .
---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Lenna.png)

![Lenna.png](Lenna.png)

How many non zero element in $\Sigma$?

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?


-----------------------------------

<sup>last modified: change your date here</sup>
