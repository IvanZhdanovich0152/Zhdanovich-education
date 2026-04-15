def find_min_penalty_path(matrix):
    if not matrix or not matrix[0]:
        return 0, []

    n = len(matrix)
    m = len(matrix[0])

    dp = [[float('inf')] * m for _ in range(n)]

    prev = [[0] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = matrix[0][j]
        prev[0][j] = -2

    for i in range(1, n):
        for j in range(m):
            candidates = []

            candidates.append((dp[i - 1][j], 0))
            if j > 0:
                candidates.append((dp[i - 1][j - 1], -1))
            if j < m - 1:
                candidates.append((dp[i - 1][j + 1], 1))

            min_penalty, direction = min(candidates, key=lambda x: x[0])

            dp[i][j] = min_penalty + matrix[i][j]
            prev[i][j] = direction

    min_penalty = min(dp[n - 1])
    end_col = dp[n - 1].index(min_penalty)

    path = []
    current_row = n - 1
    current_col = end_col

    while current_row >= 0:
        path.append((current_row, current_col))

        if current_row == 0:
            break

        direction = prev[current_row][current_col]

        if direction == -1:
            current_col -= 1
        elif direction == 0:
            pass
        elif direction == 1:
            current_col += 1

        current_row -= 1

    path.reverse()

    return min_penalty, path


def print_matrix_with_path(matrix, path):
    n = len(matrix)
    m = len(matrix[0])

    path_set = set(path)

    for i in range(n):
        print("|", end="")
        for j in range(m):
            if (i, j) in path_set:
                print(f" *{matrix[i][j]:2d}*", end="|")
            else:
                print(f" {matrix[i][j]:3d} ", end="|")
        print()
        print("-" * (m * 4 + 1))

    for i, (row, col) in enumerate(path):
        arrow = " → " if i < len(path) - 1 else ""
        print(f"({row + 1},{col + 1}){arrow}", end="")
    print()


def main():

    matrix1 = [
        [5, 2, 8, 3],
        [4, 7, 1, 9],
        [6, 3, 2, 5],
        [8, 1, 4, 7]
    ]

    min_penalty1, path1 = find_min_penalty_path(matrix1)
    print(f"Минимальный штраф: {min_penalty1}")
    print_matrix_with_path(matrix1, path1)



if __name__ == "__main__":
    main()