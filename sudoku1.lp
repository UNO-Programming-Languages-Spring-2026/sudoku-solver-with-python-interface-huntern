% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

x(1..9).
y(1..9).
n(1..9).
% Given a coordinate cell (X, Y), there must be 1, and only 1, number from n, such that sudoku is correct
{sudoku(X, Y, N) : n(N)}=1 :- x(X), y(Y).

subgrid(X, Y, 1) :- X=1..3, Y=1..3.
subgrid(X, Y, 2) :- X=1..3, Y=4..6.
subgrid(X, Y, 3) :- X=1..3, Y=7..9.
subgrid(X, Y, 4) :- X=4..6, Y=1..3.
subgrid(X, Y, 5) :- X=4..6, Y=4..6.
subgrid(X, Y, 6) :- X=4..6, Y=7..9.
subgrid(X, Y, 7) :- X=7..9, Y=1..3.
subgrid(X, Y, 8) :- X=7..9, Y=4..6.
subgrid(X, Y, 9) :- X=7..9, Y=7..9.


sudoku(X, Y, N) :- initial(X, Y, N).


% I reversed the order of these when doing a lot of other changes and dont want to risk it breaking
% So it will stay like this for the time being
:- sudoku(X,Y,N), sudoku(X,B,N), Y!=B.
:- sudoku(X,Y,N), sudoku(A,Y,N), X!=A.
:- sudoku(X,Y,N), sudoku(A,B,N), subgrid(X,Y,G), subgrid(A,B,G), (X,Y) != (A,B).

#show sudoku/3.
%#show subgrid/3.
