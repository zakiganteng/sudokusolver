from xmath import to_index, to_base
def rule0(base,  board):
    rules = []
    variables = 0
#     print ("Base:", base)
#     value = int(board[to_index(1, 0, base)])
#     print (value)
#
#     value = to_base(1 + 1, 0 + 1, value, base)
#     print(value)

    rules = []
    for j in range(0, base):
        for i in range(0, base):
            value = int(board[to_index(i, j, base)])
            value = to_base(i + 1, j + 1, value, base)
            variables += 1
            rules.append("{0} 0\n".format(value))


    ret_string = "p cnf {0} {1}\n".format(variables, variables)
    for r in rules:
        ret_string += r

    return ret_string


    # for i in range(0, base):
    #     for j in range(0, base):
    #         val = int(board[to_index(i, j, base)])
    #         if val != 0:
    #             variables += 1
    #             rules.append( str(to_base(i + 1, j + 1, val, base)) + " 0\n")
    # ret_string = 'p cnf {0} {1}\n'.format(variables, variables)
    # for r in rules:
    #     ret_string += r

    # return ret_string
