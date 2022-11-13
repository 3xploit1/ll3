from colorama import Fore, Back, Style, init
import sympy as sp
import math 


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
        self.ph = 8 * sp.ln(self.x) - 8 / 5
        
    def f(self, x):
        return 5 * x - 8 * math.log(x) - 8

    def f1(self, x):
        return 5 - 8 / x

    def newton(self, x):
        return x - self.f(x) / self.f1(x)

    def chorda(self, a, x):
        return x - self.f(x) * (x - a) / (self.f(x) - self.f(a))

    def chordb(self, x, b):
        return x - self.f(x) * (b - x) / (self.f(b) - self.f(x))

    def fi(self, x):
        return 1 + self.get_constant() * self.f1(x)


    def phi(self, x): 
        '''
        Канонический вид
        5 * x - 8 * math.log(x) - 8
        f(x) = x 
        x = 5 + 8 * math.log(x) - 8
        '''
        return 8 * math.log(x) - 8 / 5

    def get_constant(self):
        derivative_f, derivative_f_2_order, f_a, f_b, f_a_derivative, f_b_derivative, f_a_derivative_2_order, f_b_derivative_2_order = self.get_solv()
        return abs(max(f_a_derivative, f_b_derivative))/2 

    # def get_derivative_phi(self):
    #     return self.ph.diff()

    def get_fi_a(self):
        return self.fi(self.a)

    def get_fi_b(self):
        return self.fi(self.b)

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
