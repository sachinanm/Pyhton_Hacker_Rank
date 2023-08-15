#Task
#Given an integer,n, and n space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

#Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

#Input Format

#The first line contains an integer, , denoting the number of elements in the tuple.
#The second line contains  space-separated integers describing the elements in tuple .

#Output Format

#Print the result of hash(t).

#most of the solution are not exact as they didnot use of given integer n which will limit the useras it auto select the given n integers only 
# if there is any update please do connect and let me know

if __name__ == '__main__':
    n = int(input())
    t = tuple(map ( int , input().split()[:2]))
    print(hash(t))
