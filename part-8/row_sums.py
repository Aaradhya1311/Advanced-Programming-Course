def row_sums(matrix: list[list[int]]) -> list[list[int]]:
    """Calculate the sum of each row in a 2D matrix and append the sums to the respective rows.

    Args:
        matrix (list[list[int]]): A 2D list representing the matrix.

    Returns:
        list[list[int]]: The original matrix with the sums appended to each row.
    """
    for row in matrix:
        row_sum = sum(row)
        row.append(row_sum)
    return matrix


if __name__ == "__main__":
    # Example usage
    sample_matrix = [[1, 2], [3, 4]]
    row_sums(sample_matrix)
    print(sample_matrix)
