#######################################################################
#  Problem - https://leetcode.com/problems/spiral-matrix/description/ #
#  Author  - Ashish Kumar                                             #
#  Date    - 18th March, 2024                                         #
#######################################################################

class SpiralMatrix:
    def __int__(self):
        pass

    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        print(rows)
        print(cols)
        start_index = 0
        output_list = []
        while (start_index <= rows) and (start_index <= cols):
            ### single element
            print(start_index)
            print(rows)
            print(cols)
            # print(output_list)
            if start_index == cols and start_index == rows:
                output_list.append(matrix[start_index][start_index])
            # ### traverse in a row
            elif start_index == cols and start_index < rows:
                i = start_index
                while i <= rows:
                    output_list.append(matrix[i][start_index])
                    i += 1
            # ### traverse in a column
            elif start_index == rows and start_index < cols:
                i = start_index
                while i <= cols:
                    output_list.append(matrix[start_index][i])
                    i += 1
            ### make cycle
            else:
                i = start_index
                while i <= cols:
                    output_list.append(matrix[start_index][i])
                    i += 1
                i = start_index + 1
                while i <= rows:
                    output_list.append(matrix[i][cols])
                    i += 1
                i = cols - 1
                while i >= start_index:
                    output_list.append(matrix[rows][i])
                    i -= 1
                i = rows - 1
                while i > start_index:
                    output_list.append(matrix[i][start_index])
                    i -= 1
            start_index += 1
            cols -= 1
            rows -= 1
        return output_list


if __name__ == '__main__':
    m: int = 0
    n: int = 0
    m = int(input('Enter Number of list'))
    n = int(input('Enter Number of items in each list'))
    x = []
    for i in range(0, m):
        y = []
        y = input(f'Input List {i+1}').split(sep=',')
        print(y)
        if len(y) >= n:
            x.append(y[:n])
        else:
            print(f'Input List length is not as specified earlier {n}')
            break
    if len(x) == m:
        print('Here is your final input matrix')
        print(x)
        print('Processing to print the matrix in spiral form')

    else:
        print('Invalid input provided. Hence, exited.')
