# Factorial

def fun104(arg0):
    tmp109 = 0
    tmp110 = arg0 <= tmp109

    if tmp110:
        tmp111 = 1
        tmp116 = tmp111
    else:
        tmp112 = 1
        tmp113 = arg0 - tmp112
        tmp114 = fun104(tmp113)
        tmp115 = arg0 * tmp114
        tmp116 = tmp115

    return tmp116



# isPrime function 

def fun105(arg0):
    tmp117 = 1
    tmp118 = arg0 <= tmp117

    if tmp118:
        tmp119 = 0
        tmp133 = tmp119
    else:

        def fun106(arg0):
            tmp120 = 1
            tmp121 = arg0 - tmp120
            tmp122 = arg0 <= tmp121

            if tmp122:
                tmp123 = arg0 % arg0

                if tmp123:
                    tmp124 = 1
                    tmp125 = arg0 + tmp124
                    tmp126 = fun106(tmp125)
                    tmp128 = tmp126
                else:
                    tmp127 = 0
                    tmp128 = tmp127

                tmp130 = tmp128
            else:
                tmp129 = 1
                tmp130 = tmp129

            return tmp130

        tmp131 = 2
        tmp132 = fun106(tmp131)
        tmp133 = tmp132

    return tmp133

# Fibonacci Sequence 

def fun107(arg0):
    tmp134 = 1
    tmp135 = arg0 <= tmp134

    if tmp135:
        tmp143 = arg0
    else:
        tmp136 = 1
        tmp137 = arg0 - tmp136
        tmp138 = fun107(tmp137)
        tmp139 = 2
        tmp140 = arg0 - tmp139
        tmp141 = fun107(tmp140)
        tmp142 = tmp138 + tmp141
        tmp143 = tmp142

    return tmp143

print(fun104(5))
print(fun105(7))
print(fun107(9))



