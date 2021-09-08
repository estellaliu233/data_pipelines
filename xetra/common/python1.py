class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        list1 = []
        sign = 1
        number = 0
        result = 0
        for element in s:
            if element in "0123456789":
                number = number * 10 + int(element)
            elif element == "+":
                result += number * sign
                sign = 1
                number = 0
            elif element == "-":
                result += number * sign
                sign = -1
                number = 0
            elif element =="(":
                list1.append(result)
                list1.append(sign)
                sign = 1
                number = 0
                result = 0
            elif element ==")":
                result += sign * number
                sign = list1[-1]
                result = sign * result + list1[-2]
                list1 = list1[:-2]
                number = 0
                print(result,list1)
        if number != 0:
            result += number * sign
        return result
