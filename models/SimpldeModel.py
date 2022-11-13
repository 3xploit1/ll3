from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
import sympy as sp
from ll3.views.SolveView import ViewSolvData

class SimpleMethod(ViewSolvData):
    def __init__(self, e, a, b):
        super().__init__(e, a, b)    


    def set_table_simple_iteration_method(self):
        '''
        Создание объекта класса PrettyTable. Установление полей для таблицы 
        '''
        self.table_simple_iteration_method = PrettyTable()
        self.table_simple_iteration_method.field_names = [
            'n', 'x(n)', 'phi(xn)', 'delta']


    def simp_solv(self):
        n = 0 
        fixn = self.get_constant()
        # self.table_simple_iteration_method.add_row([n, xn, fixn, abs(xn - fixn)])
        while True: 
            xn = fixn 
            fixn = self.phi(xn)
            n += 1 
            self.table_simple_iteration_method.add_row([n, xn, fixn, abs(xn - fixn)])
            if (abs(xn - fixn) < self.e): 
                break
        print(self.table_simple_iteration_method)
    # def get_solve_simple_iteration_method_one_side(self):
    #     '''
    #     Односторонняя сходимость
    #     '''

    #     n = 0
    #     while abs(self.a - self.b) > self.e:
    #         a1 =
    #         self.a = a1
    #         self.b = b1
    #         n += 1
    #         self.table_combine_method.add_row([n, self.a, self.b, self.f(self.a), self.f(self.b), abs(self.a - self.b)])
    #     print(self.table_combine_method)


    # def get_solve_simple_iteration_method_one_side(self):
    #     '''
    #     Двусторонняя сходимость
    #     '''


        