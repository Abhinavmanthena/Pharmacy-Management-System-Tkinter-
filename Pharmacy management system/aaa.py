def alatrinChallenge(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)-1
    cols = len(matrix[0])-1
    max_area = 0
    heights = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0

        max_area = max(max_area, max_histogram_area(heights))

    return max_area

def max_histogram_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Input matrix as a list of strings
input_matrix = ["110", "111"]

# Convert input strings to a matrix of characters
matrix = [list(row) for row in input_matrix]

# Calculate the largest rectangle area
result = alatrinChallenge(matrix)
print(result)  # Output the result
