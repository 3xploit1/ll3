from colorama import Fore, Back, Style, init
import sympy as sp

class AbstractSolver():
    '''
    Абстрактный класс реализации 

    Аргументы: 
        - погрешность -> e 
        - левый конец интервала -> a
        - правый конец интервала -> b 
    '''

    def __init__(self, e, a, b):
        init()  # colorama
        self.e = e
        self.a = a
        self.b = b
        self.x = sp.Symbol('x')
        self.func = 5 * self.x - 8 * sp.ln(self.x) - 8
        
    def f(self, x):
        return 5 * x - 8 * sp.ln(x) - 8
    
    def get_solv(self):
        derivative_f = self.func.diff(self.x)
        derivative_f_2_order = derivative_f.diff(self.x)
        f_a = self.f(self.a)  
        f_b = self.f(self.b)
        f_a_derivative = derivative_f.subs(self.x, self.a)
        f_b_derivative = derivative_f.subs(self.x, self.b)
        f_a_derivative_2_order = derivative_f_2_order.subs(self.x, self.a)
        f_b_derivative_2_order = derivative_f_2_order.subs(self.x, self.b)
        return derivative_f, derivative_f_2_order, f_a, f_b, f_a_derivative, f_b_derivative, f_a_derivative_2_order, f_b_derivative_2_order
