def multi_bracket_validation(input):

    Round_open = input.count('(')
    Round_close = input.count(')')
    Curly_open = input.count('{')
    Curly_close = input.count('}')
    Square_open = input.count('[')
    Square_close = input.count(']')

    list_brackets =[]
    if Round_open == Round_close and Curly_open == Curly_close and Square_open == Square_close:
        if input[0] == '}' or input[0] == ')' or input[0] == ']':
            return False

        for char in input:
            if char == '{' or char == '(' or char == '[':
                list_brackets.append(char) 
            elif char == '}' or char == ')' or char == ']':
                if len(list_brackets) == 0:
                    return False
                top_element = list_brackets.pop() 
                if not Compare_brackets(top_element, char):
                    return False
        if len(list_brackets) != 0:
            return False
              
        return True

    else:
        return False



def Compare_brackets(open, close):
    if open == '(' and close == ')':
        return True
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True  
    return False

if __name__ == "__main__":
    multi_bracket_validation("{(})") 







