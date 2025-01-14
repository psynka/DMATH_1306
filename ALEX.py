# The present module works with Integer, RNumber, Polynomial, NNumber instances
# The module providing those classes is 'Dtypes.py'

from NIKITAT import DIV_ZZ_Z
from Dtypes import Integer, NNumber, Integer, RNumber, Polynomial
import Naturals, Integers, Rationals, Polynomials

def MUL_ND_N(num: NNumber, num_2: int):
    # local variables storing the value from arugments
    # avoiding changes to the original data
    list_num = num.get_num()
    length = num.get_rank()

    # 'results' will store the end result provided by the current function
    # 'keeper' is used to store the first digit if during the multiplication of two digits the product is a two digit number.
    results = []
    keeper = 0

    for i in range(length + 1):
        # 'value' stores the result of multiplication between 1 digit contained in the list and the chosen digit by the user.
        value = list_num[i] * num_2
        # When value is greater or equal to 10 it means that it contains a two digit number.
        if value < 10:
            if keeper == 0:
                results.insert(0, value)
            else:
                # the first digit of the resulting number of the multilpication is stored inside keeper
                # the value of keeper is then added to the result of the next multiplication
                value = value + keeper
                keeper = value//10
                if value < 10:
                    results.insert(0, value)
                else:
                    results.insert(0,value%10)
                    if length == i:
                        results.insert(0,keeper)
        elif keeper != 0:
            # in case the next resulting number of the multiplication also exceeds or is equal to 10
            results.insert(0, (value + keeper) % 10)
            keeper = (value+keeper) // 10
            if i == length:
                results.insert(0, keeper)
        else:
            # the second digit of the resulting number of the multiplication is stored inside of the list results
            keeper = value // 10
            results.insert(0, value % 10)
            if (length + 1) == 1:
                results.insert(0,keeper)
            elif length == i:
                results.insert(0,keeper)

    new_obj = NNumber(results)

    return new_obj


# The set of natural numbers is from 1 to infinity and does not include decimals.
# The set of integer numbers is from 0 to positive infinity as well as from 0 to negative infity.
# Therefore, any conversion of natural numbers to integer numbers will be done on the sign(positive or negative)
# depending on the user preference.
def TRANS_N_Z(num:NNumber):
    return Integer(num.get_num(), False)


#The function looks for the remainder of a division between two integers 
def MOD_ZZ_Z(num:Integer, num_2:Integer):
    #'a' stores the value of the dividend.
    #'b' stores the value of the divisor.
    #'q' stores the value of the quotient.
    #'r' stores the value of the remainder.
    
    a = Integer(num.get_num()[::-1],num.get_sign())
    b = Integer(num_2.get_num()[::-1],num_2.get_sign())
    
    # DIV_ZZ_Z FROM NIKITAT.PY
    # Finding the quotient from the division of an integer by an integer
    q = DIV_ZZ_Z(a,b)


    # MUL_ZZ_Z FROM SASHAP.PY
    # Storing the value of the divisor multiplied by the quotient
    a_1 = Integers.MUL_ZZ_Z(b,q)
    
    # Substructing the value of the divident multiplied by the quotient from the dividend
    r = Integers.SUB_ZZ_Z(a,a_1)

    # MUL_ZM_Z FROM NIKITAT.PY
    # Putting the right sign the resulting integer.
    
    if a.get_sign() == True:
        if r.get_sign() != True:
            r = Integers.MUL_ZM_Z(r)

    if (str(a) and str(b)) == '0':
        raise ZeroDivisionError("0 divided by 0")

    return r

#Substructing function(between two rational numbers)
def SUB_QQ_Q(num_1: RNumber, num_2: RNumber):
    # Вычисляем НОК (знаменатель искомой дроби)
    den = LCM_NN_N(num_1.get_den(), num_2.get_den())
    # Вычисляем числитель первой дроби после приведения к общему знаменателю
    num_1_converted = MUL_ZZ_Z(num_1.get_num(), TRANS_N_Z(DIV_NN_N(den, num_1.get_den())))
    # Вычисляем числитель второй дроби после приведения к общему знаменателю
    num_2_converted = MUL_ZZ_Z(num_2.get_num(), TRANS_N_Z(DIV_NN_N(den, num_2.get_den())))
    # Суммируем числители
    num = SUB_ZZ_Z(num_1_converted, num_2_converted)
    # Возвращаем сокращённую дробь
    return RED_Q_Q(RNumber(num, den))

#The function multiplies x^k to a polynomial
#'poly_2' should only be x^k not x^k1 + x^k2 ...
def MUL_Pxk_P(poly_1: Polynomial, poly_2: Polynomial):

    p_1 = ''
    p_2_cof = 0

    #This loop looks for the coefficient of the x^k that will be multiplied to poly_1.
    for i in poly_2.get_coefs():
        if i.get_num() != 0:
            p_2_cof = i

    #Multiplying each coefficient to one another.    
    for i in poly_1.get_coefs()[::-1]:
        p_1 += str(Rationals.MUL_QQ_Q(i,p_2_cof))
        p_1 += ' '
    p_1 = p_1[:-1]
   
   #Increasing the value of the exponents of our polynomial by k.
    for i in range(poly_2.get_exp()):
        p_1 += ' 0'
    
    return Polynomial(p_1)

#The function finds the remainder of the division between two polynomials
def MOD_PP_P(poly_1: Polynomial, poly_2: Polynomial):
    #divid will is the  dividend
    #divis will is the divisor
    divid = poly_1
    divis = poly_2

    #quotient of the division is stored inside of quo
    quo = Polynomials.DIV_PP_P(divid,divis)

    #the result of the multiplication between the divis and the quotien is stored in q_divis.
    q_divis = Polynomials.MUL_PP_P(divis,quo)

    #Once q_divis has been found it is substructed from divid(the dividend).
    res = Polynomials.SUB_PP_P(divid,q_divis)
    
    #if the remainder can still be divided by the divisor resent to the function.
    #if the remainder can't be divided anyfurther the function returns the result.
    if res.get_exp() >= divis.get_exp():
        MOD_PP_P(res,divis)
        
    return res
