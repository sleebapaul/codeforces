"""
Coin Rows - 1555C

O(N) where N is the number of columns

"""

def inp():
    """
    For taking integer inputs.
    """
    return(int(input()))

def invr():
    """
    For taking space seperated integer variable inputs.
    """
    return(list(map(int,input().split())))


def score(matrix):
    first_row_sum = sum(matrix[0])
    second_row_sum = 0

    max_score = float("inf")
    for i in range(len(matrix[0])):
        sum_one = first_row_sum - matrix[0][i]
        if  first_row_sum - matrix[0][i] != 0:
            first_row_sum -= matrix[0][i]

        sum_two = second_row_sum
        second_row_sum += matrix[1][i]

        max_score = min(max_score, max(sum_one, sum_two))
    print(max_score)


n = inp()
matrices = []
for  i in range(n):
    m = inp()
    tmp = []
    for _ in range(2):
        line = invr()
        tmp.append(line)
    matrices.append(tmp)

for matrix in matrices:
    score(matrix)


