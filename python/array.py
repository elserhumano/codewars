def solution(A):
    # write your code in Python 3.6

    # Remove duplicate
    A = list(dict.fromkeys(A))
    print('Without repeated: ',A)

    A.sort()
    print('Ordered: ', A)

    the_max = max(A)
    print('Max of array: ', the_max)

    if the_max < 0:
      return 1

    for i in range(1, the_max + 2):
      print(i)
      if not i in A:
        return i


# print(solution([5,-4,-3,1,5,4,2,1]))
# print(solution([3,2,1]))
print(solution([-3,-1]))
