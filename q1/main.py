def overlaps(first_line, second_line):
    found = False
    result = str(first_line) + ' & ' + str(second_line) + ' do not overlaps on x-axis'
    index_position = 0
    for i in range(2):
        if first_line[i] < 0 and second_line[i] < 0:
            while index_position < len(first_line) and not found:
                if second_line[index_position] >= first_line[0] or second_line[index_position] >= first_line[1]:
                    found = True
                    result = str(first_line) + ' & ' + str(second_line) + ' overlaps on x-axis'
                else:
                    index_position += 1
        else:
            while index_position < len(first_line) and not found:
                if second_line[index_position] <= first_line[0] or second_line[index_position] <= first_line[1]:
                    found = True
                    result = str(first_line) + ' & ' + str(second_line) + ' overlaps on x-axis'
                else:
                    index_position += 1
    return result


if __name__ == '__main__':
    first_line = []
    second_line = []
    try:
        for i in range(2):
            first_axis = int(input('{0}.Please enter first line of x-axis: \n'.format(i + 1)))
            first_line.append(first_axis)
        for i in range(2):
            second_axis = int(input('{0}.Please enter second line of x-axis: \n'.format(i + 1)))
            second_line.append(second_axis)

        result = overlaps(first_line, second_line)
        print("\n",result)

    except ValueError:
        print('Please enter numeric value, no other value is valid\n'
              "Please Enter two co-ordinates on each Line")