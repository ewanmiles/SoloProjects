#######################################################################################################################################################################

# FIRST DERIVATIVE CALCULATOR #
# Incorporated: basic variables ("x"), e, ln, sin, cos, tan, csc, cot, sec, arctan, arccos, arcsin, quotients ("x/y")

# This is a long script and thus, depending on your processor, will run slowly after around 150-200 inputs.
# It is suggested you re-run either the kernel or the script at this stage to clear the terminal and return to the fastest speeds.

# All expressions should ONLY be input in STRING format, i.e. "4x^2", with quote marks, not 4x^2.

# The diff(x) function has incorporated all sub-functions for derivatives and can differentiate any of the variables/functions above.
# Surrounding the expression with brackets will stop the code from working, i.e. diff("(x^2)") will not return your derivative.

# There is a Maclaurin Expansion function being built at the bottom of the script. It currently has little capability beyond basics, but feel free to test it.

# Any 'check' functions work by slicing strings according to what is being sought.
# e.g. coeffcheck(x) will slice the string to look for the coefficient, varcheck(x) will look for the subject variable (often "x"), etc.

# The code has been developed to be as bracket-independable as possible, i.e. diff("(-2)sin(-2x)") and diff("-2sin-2x") should output the same derivative.
# THIS DOES COUNT on the user not incorporating brackets into strange places, e.g. diff("2(sin)4x")

# Many functions incorporate other functions, which in turn incorporate the first function, which means it can't all just be run in one cell.
# The best approach is to run the whole code as a cell, then run the diff(x) function, following what you need to run after each error you run into.

#######################################################################################################################################################################

import math
import time

def string_iteration(y):
    ### Function that iterates over each character in a string and returns any non-digit characters in a string ###
    ### e.g. "tan(2x^2)" -> "tan(x^)" ###
    index = 0
    # While loop checks each character, replaces any digits with empty strings
    while index < len(y): 
        character = y[index] #slices y to return character at index
        if character.isdigit() == True:
            y = y.replace(character, "")
        else:
            index += 1  #move to next string index
    return y

string_iteration("")

def arrange(y):
    ### Function to remove each index in an array that takes the value -1, then organises the list in rising numerical order ###
    ### Used mainly for returning and ordering a list of functions ###
    ### e.g. arrange([-1,4,2,-1,-1,5,-1,-1]) -> [2,4,5] ###
    index = 0
    length = len(y)
    while index < length:
        number = y[index]
        if number == -1:
            y.remove(number)   #remove a -1 element
            length -= 1   #change length as an element has been removed, others ahead move left
            continue
        index += 1
    # Arrange in rising numerical order
    y.sort()
    return y

arrange([-1,4,2,-1,-1,5,-1,-1])

def general_replace(x, y, z):
    ### Function that iterates over a list replacing any elements 'x' with 'y' ###
    # e.g. general_replace(4,5,[1,3,5,4,6,9,4,5]) -> [1,3,5,5,6,9,5,5]
    if isinstance(z,list) == True:
        index = 0
        while index < len(z):
            term = z[index]
            if term == x:
                z[index] = y
            index += 1
    else:
        z = z.replace(x,y)
    return z

general_replace("x","y","xyz")

def specific_replace(x, y):
    ### Function to replace ALL INSTANCES OF A STRING featured in a list with that string only ###
    ### WARNING - function does not work if list includes integers ###
    # e.g. specific_replace(['sinx','cosx',2], 'cos') -> ['sinx','cos',2] 
    # e.g. specific_replace(['actually','no','its','impossible'], 'i') -> ['actually','no','i','i']
    function = [s for s in x if y in s]   #find all instances of string in elements
    index = 0
    while index < len(function):   #iterate through elements
        x = general_replace(function[index],y,x)   #replace instances of string with desired string
        index += 1
    return x

specific_replace(['actually','no','its','impossible'], 'i')

def function_replace(y):
    ### Function that checks all functions in a list and replaces them with JUST the function ###
    # e.g. function_replace(['sinx','cos5x','2x']) -> ['sin','cos','2x']
    # Search for each function string
    sin = [s for s in y if 'sin' in s]
    cos = [s for s in y if 'cos' in s]
    tan = [s for s in y if 'tan' in s]
    arcsin = [s for s in y if 'arcsin' in s]
    arccos = [s for s in y if 'arccos' in s]
    arctan = [s for s in y if 'arctan' in s]
    cot = [s for s in y if 'cot' in s]
    sec = [s for s in y if 'sec' in s]
    csc = [s for s in y if 'csc' in s]
    ln = [s for s in y if 'ln' in s]
    if arcsin != []:
        y = specific_replace(y, 'arcsin')
    if arccos != []:
        y = specific_replace(y, 'arccos')
    if arctan != []:
        y = specific_replace(y, 'arctan')
    if sin != []:
        for i in sin:
            if 'arcsin' in i:
                continue
            elif i in y:
                index = y.index(i)
                y[index] = 'sin'
    if cos != []:
        for i in cos:
            if 'arccos' in i:
                continue
            elif i in y:
                index = y.index(i)
                y[index] = 'cos'
    if tan != []:
        for i in tan:
            if 'arctan' in i:
                continue
            elif i in y:
                index = y.index(i)
                y[index] = 'tan'
    if ln != []:
        y = specific_replace(y, 'ln')
    if cot != []:
        y = specific_replace(y, 'cot')
    if csc != []:
        y = specific_replace(y, 'csc')
    if sec != []:
        y = specific_replace(y, 'sec')
    return y
        #e.g. arctan and tan both produce != -1 thus the condition has to be more explicit

function_replace(['cosx','sinx','arcsint'])

def functioncheck(y):
    ### Function to return mathematical function used in an expression ###
    ### e.g. sin, cos, tan, ln, etc ###
    y = str(y)
    function = [] #open an array to add functions to if multiple or single
    # Search for each function string
    sin = y.find("sin")
    cos = y.find("cos")
    tan = y.find("tan")
    arcsin = y.find("arcsin")
    invsin = y.find("sin^-1")
    arccos = y.find("arccos")
    invcos = y.find("cos^-1")
    arctan = y.find("arctan")
    invtan = y.find("tan^-1")
    cot = y.find("cot")
    csc = y.find("csc")
    sec = y.find("sec")
    ln = y.find("ln")
    #e.g. arctan and tan both produce != -1 thus the condition has to be more explicit
    # Introduce a count so it returns how many functions are in the check
    function.append(sin)
    function.append(cos)
    function.append(tan)
    function.append(arcsin)
    function.append(invsin)
    function.append(arccos)
    function.append(invcos)
    function.append(arctan)
    function.append(invtan)
    function.append(cot)
    function.append(csc)
    function.append(sec)
    function.append(ln)
    function = arrange(function)
    func = []
    index = 0
    while index < len(function):
        term = function[index]
        if term == function[len(function) - 1]:
            func.append(y[term:])
        else:
            nextterm = function[(index+1)]
            func.append(y[term:nextterm])
        index += 1
    func = function_replace(func)
    if len(function) > 1:       
        func.append(len(function)) #append the array of functions with the count if two or more are found
    elif len(function) == 0:
        func = "" #return an empty string if no function is found
    else:
        func = str(func[0])  #return the function as a string if only one is found
    return func

functioncheck("arctanxsinx")

def varcheck(y):
    ### Function that cuts the input string to return the variable from an expression ###
    e = y.find("e^")
    func = functioncheck(y)
    if e != -1:
        y = "e"
    else:
        openingbracket = y.find("(")
        closingbracket = y.find(")")
        if openingbracket == 0:
            opened = closingbracket + 1
            y = y[opened:]
        y = string_iteration(y)
        #check is function is a list (i.e. multiple functions), carry out role on each one by iterating through list
        if isinstance(func, list) == True:
            index = 0
            while index < (len(func)-1):  #iterate over every function in array but NOT count
                function = func[index]
                y = y.replace(function, "")
                index += 1
        else:
            y = y.replace(func,"")
        y = y.replace("(","")
        y = y.replace(")","")
        y = y.replace("^","")
        y = y.replace("-","")
        y = y.replace("+","")
        if len(y) > 1:
            y = y[0]
    return y

varcheck("(x^2)(e^2x^2)")

def coeffcheck(y):
    ### Function to return a coefficient from an expression ###
    ### CANNOT be used on a multifunction expression, e.g. sinxcosx ###
    openingbracket = y.find("(")
    closingbracket = y.find(")")
    if openingbracket == 0:
        opened = openingbracket + 1
        closed = closingbracket
        y = y[opened:closed]
        print(y)
    negative = y.find("-")
    if negative == 0:
        y = y[1:]
        print(y)
    index = 0
    while index < len(y):
        character = y[index]
        if character.isdigit() == False:
            y = y[:index]
            break
        index += 1
    if negative != -1:
        y = "-" + y
    return y

coeffcheck("(25tanxsinx)")

def powercheck(y):
    ### Function to return the first power from an expression ###
    # Removing ^-1 arc trig notation to stop confusion with exponent "^"
    y = str(y)
    func = functioncheck(y)
    if func == "arctan":
        y = y.replace("tan^-1","")
    if func == "arcsin":
        y = y.replace("sin^-1","")
    if func == "arccos":
        y = y.replace("cos^-1","")
    var = varcheck(y)
    varpos = y.find(var)
    y = y[varpos:]
    exponent = y.find("^")
    if exponent != -1:
        powerpos = int(exponent + 1)
        bracketcheck = y.find("(")
        if bracketcheck == -1:
            return y[powerpos:]
        else:
            opened = int(exponent + 2)
            closed = len(y) - 1
            return y[opened:closed]

powercheck("")

def variable_cancel(numerator, denominator):
    ### Function to cancel variables with powers to simplify fractions ###
    ### i.e. "5x^3/2x^4" -> "5/2x" ###
    num = varcheck(numerator)
    denom = varcheck(denominator)
    n_co = coeffcheck(numerator)
    d_co = coeffcheck(denominator)
    if num == denom and num != "" and num != None and denom != "" and denom != None:
        n_power = powercheck(numerator)
        d_power = powercheck(denominator)
        #convert to integers for working new powers
        #need if statement for checking dtype as int(NoneType) does not compute
        if n_power == None or n_power == "":
            n_power = 0
        else:
            n_power = int(n_power)
        if d_power == None or d_power == "":
            d_power = 0
        else:
            d_power = int(d_power)
        if n_power > d_power:
            denominator = d_co
            if d_power == 0:
                new_power = n_power
                new_power -= 1
            else:
                new_power = n_power - d_power
            if new_power <= 1:
                #cut off coefficient and reattach later to stop it from being replaced if power is the same
                numerator = numerator.replace("^","")
                coeffpos = numerator.find(n_co)
                numerator = numerator[(coeffpos+len(n_co)):]
                numerator = numerator.replace(str(n_power),"")
                numerator = n_co + numerator
            else:
                coeffpos = numerator.find(n_co)
                numerator = numerator[(coeffpos+len(n_co)):]
                numerator = numerator.replace(str(n_power),str(new_power))
                numerator = n_co + numerator
        elif d_power > n_power:
            numerator = n_co
            if n_power == 0:
                new_power = d_power
                new_power -= 1
            else:
                new_power = d_power - n_power
            if new_power <= 1:
                #cut off coefficient and reattach later to stop it from being replaced if power is the same
                denominator = denominator.replace("^","")
                coeffpos = denominator.find(d_co)
                denominator = denominator[(coeffpos+len(d_co)):]
                denominator = denominator.replace(str(d_power),"")
                denominator = d_co + denominator
            else:
                coeffpos = denominator.find(d_co)
                denominator = denominator[(coeffpos+len(d_co)):]
                denominator = denominator.replace(str(d_power),str(new_power))
                denominator = d_co + denominator
        elif n_power == d_power:
            numerator = n_co
            denominator = d_co
    if numerator == "":
        numerator = "1"
    if denominator == "":
        cancelled = "{0}".format(numerator)
    else:
        cancelled = "{0}/{1}".format(numerator,denominator)
    return cancelled

variable_cancel("-9x^5","-x")

def simplify(numerator, denominator):
    ### Function that simplifies fractions using highest common factor ###
    # Simplify has a built in timer that cancels the for loop after 10 seconds of iteration
    # If it breaks after 10s it returns the last hcf found and simplifies the fraction
    # This is to stop very long unnecessary iteration for higher order Maclaurin approximations
    top = coeffcheck(numerator)
    bottom= coeffcheck(denominator)
    num_var = varcheck(numerator)
    denom_var = varcheck(denominator)
    top_pwr = powercheck(numerator)
    bot_pwr = powercheck(denominator)
    top_func = functioncheck(numerator)
    bot_func = functioncheck(denominator)
    #return x if top function and bottom function not the same i.e. sinx/lnx
    #also return x if top var and bottom var not the same but functions are the same i.e. sinx/sint
    if (top_func != bot_func or ((top_func == bot_func) and top_func != "" and (num_var != denom_var))) and top_func != "" and bot_func != "":
        x = str(numerator) + "/" + str(denominator)
        return x
    if top == "" or bottom == "":
        x = variable_cancel(numerator, denominator)
        return x
    else:
        num_coefficient = int(top)
        denom_coefficient = int(bottom)
    newhcf = 1  #set default divisor to 1 in case it escapes the loop for whatever reason
    start_time = time.time()   #timer to break for loop if it goes on too long, giving current hcf
    for i in range(1, abs(num_coefficient*denom_coefficient)):  #abs() for inclusion of negative coefficients
        if num_coefficient % i == 0 and denom_coefficient % i == 0:
            newhcf = i
        new_time = time.time()
        if new_time - start_time > 10:
            break
    new_num_co = int(num_coefficient/newhcf)
    if new_num_co == 1 and num_var != "":
        new_num_co = ""
    elif new_num_co == -1 and num_var != "":
        new_num_co = "-"
    new_denom_co = int(denom_coefficient/newhcf)
    if new_denom_co == 1 and (denom_var != "" or denom_var != None):
        new_denom_co = ""
    elif new_denom_co == -1 and (denom_var != "" or denom_var != None):
        new_denom_co = "-"
    numerator = str(numerator)
    if top_pwr != "" and top_pwr != None:
        if num_var == "e":
            pass
        else:
            exponent = numerator.find("^")
            numerator = numerator[:exponent]
            numerator = numerator.replace(top,str(new_num_co))
            numerator = numerator + "^" + top_pwr
    else:
        numerator = numerator.replace(top,str(new_num_co))
    denominator = str(denominator)
    if bot_pwr != "" and bot_pwr != None:
        if denom_var == "e":
            pass
        else:
            exponent = denominator.find("^")
            denominator = denominator[:exponent]
            denominator = denominator.replace(bottom,str(new_denom_co))
            denominator = denominator + "^" + bot_pwr
    else:
        denominator = denominator.replace(bottom, str(new_denom_co))
    #final check of coefficients to prevent negative over negative, i.e. fix -1/-x -> 1/x
    top_negative = numerator.find("-")
    bottom_negative = denominator.find("-")
    if top_negative == bottom_negative == 0:
        numerator = numerator[1:]
        denominator = denominator[1:]
    elif bottom_negative == 0 and top_negative != 0:
        numerator = "-" + numerator
        denominator = denominator[1:]
    x = variable_cancel(numerator, denominator)
    return x

simplify("32sin2x","24")

def coeff_multiply(x, multiplier):
    ### Function that multiplies the coefficient of an argument, x, by a multiplier, returning the full expression as a string ###
    # e.g. coeff_multiply("7e^2x", "2") -> "14e^2x"
    x_coeff = coeffcheck(x)  #takes coefficient of expression
    power = powercheck(x)
    if x_coeff == "-1" and multiplier == "-1":
        negative = x.find("-")
        x = x[(negative+1):]
        return x
    elif (x_coeff == "" or x_coeff == None) and multiplier == "-1":
        x = "-" + x
        return x
    if multiplier != None and x_coeff != "":
        x_coeff = coeffcheck(x_coeff)  #first coefficient may include a variable so takes coefficient again
        new_coeff = str(int(x_coeff) * int(multiplier))
        new_coeff = str(new_coeff)
        x = x.replace(x_coeff, new_coeff)
        new_power = powercheck(x)
        if new_power != power:
            x = x.replace(new_power, power) #if coeff_multiply replaces original power, change it back
    elif multiplier != None and x_coeff == "":
        new_coeff = str(multiplier)
        opened = x.find("(")
        if opened == 0:
            add_x = x[1:] 
            x = new_coeff + add_x
        else:
            x = new_coeff + x
    double_negative = x.find("--")
    if double_negative != -1:
        x = x.replace("--","")
    return x

coeff_multiply("","")

def square(x):
    ### Function that squares an expression with a coefficient and power ###
    # Used for, e.g. square("2x^3") -> "4x^6", square("10") -> "100"
    function = functioncheck(x)
    if function != "":
        funcpos = x.find(function)
        replace_index = funcpos + len(function)
        start = x[:replace_index]
        end = x[replace_index:]
        x = start + "^2" + end
    else:
        var = varcheck(x)
        x_coeff = coeffcheck(x)
        if x_coeff != "":
            x_coeff = int(x_coeff)
            x_coeff = x_coeff ** 2
        x_power = powercheck(x)
        if x_power != "" and x_power != None:
            x_power = int(x_power)
            x_power *= 2
            x = "{0}{1}^{2}".format(x_coeff,var,x_power)
        elif (var != "" and var != None) and (x_power == "" or x_power == None):
            x_power = "2"
            x = "{0}{1}^{2}".format(x_coeff,var,x_power)
        else:
            x = "{0}{1}".format(x_coeff,var)
    return x

square("")

def multiply(x, y):
    ### Function that multiplies two expressions together into a single term ###
    ### NOTE: Input expressions must share the same variable, e.g. e^x cannot multiply with x ###
    # Do not use this to multiply and expression by a number. For that, use coeff_multiply(x, multiplier)
    # Used for, e.g. multiply("2x", "5x^2") -> "10x^3"
    x_co = coeffcheck(x)
    y_co = coeffcheck(y)
    if y_co != "" and x_co != "" and y_co.isdigit() == True and x_co.isdigit() == True:
        new_co = coeff_multiply(x_co, y_co)
    elif y_co != "" and x_co != "" and (y_co.isdigit() == True or x_co.isdigit() == True):
        x_var = varcheck(x_co)
        y_var = varcheck(y_co)
        if x_var != "" and x_var != None:
            new_co = coeff_multiply(x_co, y_co)
        elif y_var != "" and y_var != None:
            new_co = coeff_multiply(y_co, x_co)
    elif y_co != "" and x_co != "" and y_co.isdigit() == False and x_co.isdigit() == False:
        new_co = multiply(x_co, y_co)
    elif y_co != "" and x_co == "":
        new_co = coeff_multiply(x_co, y_co)
    elif x_co != "" and y_co == "":
        new_co = coeff_multiply(y_co, x_co)
    else:
        new_co = ""
    x_power = powercheck(x)
    y_power = powercheck(y)
    var = varcheck(x)
    if var == "e":
        x_p_var = varcheck(x_power)
        y_p_var = varcheck(y_power)
        if x_p_var == y_p_var:
            y_p_co = coeffcheck(y_power)
            x_p_co = coeffcheck(x_power)
            if y_p_co != "" and x_p_co != "":
                new_power = str(int(x_p_co) + int(y_p_co)) + x_p_var
            elif y_p_co != "" and x_p_co == "":
                new_power = str(int(y_p_co) + 1) + x_p_var
            elif x_p_co != "" and y_p_co == "":
                new_power = str(int(x_p_co) + 1) + x_p_var
            else:
                new_power = "2" + x_p_var
    else:
        if x_power != None and x_power != "" and y_power != None and y_power != "":
            new_power = str(int(x_power) + int(y_power))
        elif x_power != None and x_power != "" and (y_power == None or y_power == ""):
            new_power = str(int(x_power) + 1)
        elif y_power != None and y_power != "" and (x_power == None or x_power == ""):
            new_power = str(int(y_power) + 1)
        else:
            new_power = "2"
    output = new_co + var + "^" + new_power
    return output

multiply("6e^x","5x^3")

def inverse_power(x):
    ### Function to fix powers on the bottom of fractions after differentiating ###
    # It essentially raises the power of the denominator by 1
    # e.g. inverse_power("-4/x^2") -> "-4/x^3"
    quotient = x.find("/")
    if quotient != -1:
        top = x[:quotient]
        top_var = varcheck(top)
        bottom = x[(quotient+1):]
        bottom_var = varcheck(bottom)
    else:
        bottom_var = ""
    if bottom_var != "" and bottom_var != "e":
    #if x is on bottom, slice off power, reduce it, re-attach it
        if top_var != "" and top_var != None:
            x = simplify(top, bottom)
        exponent = bottom.find("^")
        if exponent != -1:
            exponent += (len(top) + 1)
            power = int(powercheck(bottom))
            new_power = power + 1
            before = x[:(exponent + 1)]
            x = before + str(new_power)
    return x

inverse_power("-5/x^5")

def basicdiff(x):
    ### Function that returns the derivative of a basic expression only containing one variable ###
    ### e.g. 12x^6 -> 72x^5, cannot do e, trig, etc ###
    var = varcheck(x)
    power = powercheck(x)
    coefficient = coeffcheck(x)
    if len(x) == 1 and var != "" and var != None:
        x = "1"
    elif (coefficient != 0 and coefficient != None and coefficient != "") and (power != 0 and power != None and power != ""):
        if power == "2":
            coefficient = int(coefficient) * int(power)
            x = "{0}{1}".format(coefficient,var)
        else:
            coefficient = int(coefficient) * int(power)
            power = int(power) - 1
            x = "{0}{1}^{2}".format(coefficient,var,power)
    elif power == "" or power == None and var!= "" and var != None:
        var = ""
        x = coefficient
    elif (coefficient == 0 or coefficient == None or coefficient == "") and (power != 0 and power != None and power != ""):
        coefficient = power
        if power == "2":
            x = "{0}{1}".format(coefficient,var)
        else:
            power = int(power) - 1
            x = "{0}{1}^{2}".format(coefficient,var,power)
    else:
        return None
    return x

basicdiff("53x^45")

def ediff(coeff, pwr):
    ### Function that returns the derivative an expression containing only e and one variable ###
    ### e.g. 5e^7x -> 35e^7x, 10e^(2x^6) -> (120x^5)e^(2x^6), cannot do product, quotient, etc ###
    ### Takes arguments for the coefficient and power of e ###
    new_coefficient = "("+diff(pwr)+")"
    if new_coefficient == "(1)":
        new_coefficient = ""
    elif new_coefficient == "(-1)":
        if coeff == "-" or coeff == "-1":
            new_coefficient = ""
            x = "{0}e^({1})".format(new_coefficient,pwr)
            return x
        else:
            multiplier = "-1"
            new_coefficient = coeff_multiply(coeff, multiplier)
            x = "{0}e^({1})".format(new_coefficient,pwr)
            return x
    x = "{0}e^({1})".format(new_coefficient,pwr)
    if coeff != "" and coeff != None:
        if coeff == "-":
            multiplier = "-1"
        else:
            multiplier = coeff
        x = coeff_multiply(x,multiplier)
    return x

ediff("", "")

def functiondiff(x, function):
    ### Function that calculates the derivative of multiple mathematical functions ###
    ### e.g. sin, cos, tan, ln ###
    # NOTE: This function contains the diff function, which is written after it.
    # The diff function also contains this functiondiff function.
    # Thus, to use both properly, run functiondiff -> run diff -> run functiondiff again. 
    multiplier = None
    coefficient = coefficient(x)
    if coefficient != "":
        multiplier = coefficient
        funcpos = x.find(function)
        # If searching for ^-1 notation, slice "arc" and add "^-1", then repair after index is found
        if funcpos == -1:
            function = function[3:] + "^-1"
            funcpos = x.find(function)
            function = "arc" + function[:3]
        x = x[funcpos:]
    arc_check = x.find("^-1")
    if arc_check != -1:
        if function == "arcsin":
            x_new = x.replace("sin^-1","")
        elif function == "arccos":
            x_new = x.replace("cos^-1","")
        elif function == "arctan":
            x_new = x.replace("tan^-1","")
    else:
        x_new = x.replace(function,"")
    x_new = x_new.replace("(","")
    x_new = x_new.replace(")", "")
    if function == "ln":
        top = diff(x_new)
        top = coeff_multiply(top, multiplier)
        bottom = x_new
        x = simplify(top,bottom)   
    elif function == "arcsin":
        top = diff(x_new)
        top = coeff_multiply(top, multiplier)
        squared = square(x_new)
        bottom = "√(1 - {0})".format(squared)
        x = "({0})/({1})".format(top,bottom)
    elif function == "arccos":
        top = diff(x_new)
        top = coeff_multiply(top, multiplier)
        squared = square(x_new)
        bottom = "√(1 - {0})".format(squared)
        x = "-({0})/({1})".format(top,bottom)
    elif function == "arctan":
        top = diff(x_new)
        top = coeff_multiply(top, multiplier)
        squared = square(x_new)
        bottom = "{0} + 1".format(squared)
        x = "({0})/({1})".format(top,bottom)
    else:
        new_co = diff(x_new)
        new_co = coeff_multiply(new_co, multiplier)
        #check if the new_co is "-1", if it is, replace it with just "-"
        final_co = coeffcheck(new_co)
        if final_co == "-1":
            new_co = "-"
        if new_co != "1":
            x = new_co + x
        if function == "sin":
            x = x.replace("sin","cos")
        elif function == "cos":
            x = x.replace("cos","sin")
            x = "-" + x
        elif function == "tan":
            x = x.replace("tan","sec^2")
        elif function == "cot":
            x = x.replace("cot","csc^2")
            x = "-" + x
        elif function == "sec":
            x = x + "tan(" + x_new + ")"
        elif function == "csc":
            x = x + "cot(" + x_new + ")"
            x = "-" + x
        double_negative = x.find("--")  #Search for double negative to change e.g. --sin -> sin
        if double_negative != -1:
            x = x.replace("--","")
    return x

functiondiff("","")

def quotientdiff(top, bottom):
    ### Function that calculates the derivative of a quotient (fraction) ###
    ### CURRENTLY NEEDS AN OVERHAUL ###
    u = top
    v = bottom
    du = diff(u)
    dv = diff(v)
    v_squared = square(v)
    #gather variable from all terms to see if two terms can multiply to make a single term
    #i.e. to check if u*dv can form one term instead of two bracketed terms
    u_var = varcheck(u)
    v_var = varcheck(v)
    du_var = varcheck(du)
    dv_var = varcheck(dv)
    if v_var == du_var and v_var != "" and v_var != None:
        vdu = multiply(v,du)
    elif du == None:
        vdu = ""
    elif du.isdigit() == True or (du.isdigit() == True and v.isdigit() == True):
        vdu = coeff_multiply(v,du)
    elif v.isdigit() == True:
        vdu = coeff_multiply(du,v)
    else:
        vdu = "({0})({1})".format(v,du)
    if u_var == dv_var and u_var != "" and u_var != None: 
        udv = multiply(u,dv)
    elif dv == None:
        udv = ""
    elif dv.isdigit() == True or (dv.isdigit() == True and u.isdigit() == True):
        udv = coeff_multiply(u,dv)
    elif u.isdigit() == True:
        udv = coeff_multiply(dv,u)
    else:
        udv = "({0})({1})".format(u,dv)
    if udv != "" and vdu != "":
        x = "{0}-{1}/{2}".format(vdu,udv,v_squared)
    elif udv == "" and vdu != "":
        x = "{0}/{1}".format(vdu,v_squared)
    elif udv != "" and vdu == "":
        x = "-{0}/{1}".format(udv,v_squared)
    double_negative = x.find("--")
    if double_negative != -1:
        x = x.replace("--","")
    return x

quotientdiff("x","2x^2")

diff("e^2x")

def productdiff(x):
    terms = []  #start an empty array to fill with each term in the product
    openingbracket = x.find("(")
    closingbracket = x.find("(")
    func = functioncheck(x)
    var = varcheck(x)
    coefficient = coeffcheck(x)
    if isinstance(func,list) == True: #multiple functions diff
        index = 0
        while index < len(func):
            item = func[index] #searching for string found in this index in func array
            if isinstance(item, int) == True:
                terms.append(x) #if it reaches the count in the func array, add x to the terms array as it is only the final term now
                break
            pos = x.find(item) #find that string (i.e. function) in x
            if index == 0:
                coefficient = x[:pos] #when on the first function, what comes before must be the coefficient
                x = x[pos:]
                index += 1
            else:
                terms.append(x[:pos]) #add what is previous to this function to terms array as a term
                x = x[pos:] #slice off previous term so that we do not include the previous term in each new term
                index += 1 #continue to iterate over each function
    elif var == "e" and func != "": #e and function diff
        funcindex = x.find(func)
        eindex = x.find(var)
        if eindex < funcindex:
            coefficient = x[:eindex]
            eterm = x[eindex:funcindex]
            functerm = x[funcindex:]
        elif funcindex < eindex:
            coefficient = x[:funcindex]
            eterm = x[eindex:]
            functerm = x[funcindex:eindex]
        terms.append(eterm)
        terms.append(functerm)
    elif var == "e" and func == "":
        colength = len(coefficient)
        x = x[colength:]
        e = x.find("e^")
        index = 0
        indices = []
        while index < len(x):
            character = x[index]
            if character == "x":
                indices.append(index)
            index += 1
        if len(indices) > 1:
            indices.append(e)
            indices.sort()
            if e == indices[0]:
                coefficient 
                xpos = x[indices[2]:]
                if x[indices[2]-1] == "(":
                    xpos = x[indices[2]-1:]
                epos = x[:x.find(xpos)]
            elif e == indices[1]:
                xpos = x[:e]
                epos = x[e:]
                if x[e-1] == "(":
                    xpos = x[:e-1]
                    epos = x[e-1:]
        terms.append(xpos)
        terms.append(epos)
    u = terms[0]
    v = terms[1]
    du = diff(u)
    dv = diff(v)
    x = "{0}({1})({2})+{0}({3})({4})".format(coefficient,u,dv,v,du)
    return x

productdiff("25(e^2x)(2x)")

coeffcheck("(25x^2e^2x)")

varcheck("sinxtanx")

functioncheck("sinx")

coeffcheck("sinxtanx")

def diff(x):
    ### Gathers all derivative-finding functions into one to accept any expression by routing it through the correct function ###
    ### e.g. it can handle trig, basic, e, ln, etc ###
    var = varcheck(x)
    power = powercheck(x)
    coefficient = coeffcheck(x)
    if coefficient == "0" or coefficient == 0:
        return None
    function = functioncheck(x)
    quotient = x.find("/")
    #try statement to return None for any numbers or fractions
    try:
        #if a fraction, try and make top and bottom integers, if possible return None
        if quotient != -1:
            top = x[:quotient]
            bottom = x[(quotient + 1):]
            int(top)
            int(bottom)
            return None
        #if not a fraction, try and make x an integer, if possible return None
        else:
            int(x)
            return None
    except ValueError:
        if quotient != -1:
            top = x[:quotient]
            bottom = x[(quotient + 1):]
            try:
                #check if quotient can be simplified and differentiated otherwise
                simplified = simplify(top, bottom)
                quotientcheck = simplified.find("/")
                #if still quotient, simplify and use quotientdiff
                if quotientcheck != -1:
                    q_top = simplified[:quotientcheck]
                    q_bottom = simplified[(quotientcheck + 1):]
                    #if cancelled to simple number fraction, return None
                    if q_top.isdigit() == True and q_bottom.isdigit() == True:
                        x = None
                    else:
                        #check if still quotient and attempt to simplify answer
                        x = quotientdiff(q_top, q_bottom)
                        quotientcheck = x.find("/")
                        if quotientcheck != -1:
                            q_top = x[:quotientcheck]
                            q_bottom = x[(quotientcheck + 1):]
                            try:
                                x = simplify(q_top, q_bottom)
                            except:
                                pass
                #if the simplification removed the quotient, differentiate normally
                else:
                    x = diff(simplified)
            except:
                x = quotientdiff(top, bottom)
                x = inverse_power(x)
        elif function != "":
            if isinstance(function, list) == True:
                x = productdiff(x)
            else:
                x = functiondiff(x, function)
        elif len(var) == 1 and var != "e" and var.isdigit() == False:
            x = basicdiff(x)
        elif var == "e":
            x = ediff(coefficient,power)
        return x

### Will not work if you surround the expression with brackets e.g. (sin4x), (2x^2)
diff("(5x)/(5-x)") 

def maclaurin_expand(x, order):
    term = 0
    #if user inputs order as a string, convert to integer
    if isinstance(order, str) == True:
        order = int(order)
    for term in range(order+1):
        if term == 0:
            #if quotient, simplify if possible
            quotient = x.find("/")
            if quotient != -1:
                top = x[:quotient]
                bottom = x[(quotient + 1):]
                x = simplify(top,bottom)
            print(x)
        elif term == 1:
            x = diff(x)
            if x[0] == "-":
                print("({0})(x)".format(x))
            else:
                print("+({0})(x)".format(x))
        else:
            x = diff(x)
            top = "({0})(x^{1})".format(x,term)
            bottom = math.factorial(term)
            newterm = simplify(x, bottom)
            newterm = "{0}(x^{1})".format(newterm,term)
            #break from series if a derivative turns up None i.e. diff(4) -> None
            nonecheck = newterm.find("None")
            if nonecheck != -1:
                print("Series finished (cannot differentiate further)")
                break
            cut_newterm = newterm.replace("(","")
            cut_newterm = cut_newterm.replace(")","") 
            cut_newterm = cut_newterm.replace(" ","")
            if cut_newterm[0] == "-":
                print(newterm)
            else:
                print("+{0}".format(newterm))
        term += 1

maclaurin_expand("lnx","4")

functioncheck("cosxsinx")
