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

    def check_convergence(self):
        if (self.get_phi_a() or self.get_phi_b() < 0 ): 
            self.get_solve_simple_iteration_method_two_side()
        elif ((self.get_phi_a() or self.get_phi_b()) > 0 ):
            self.get_solve_simple_iteration_method_monoton()
               
    def get_solve_simple_iteration_method_monoton(self):
        '''
        Монотонная сходимость 
        '''
        n = 0
        xn = self.a 
        fixn = self.phi(xn)
        self.table_simple_iteration_method.add_row([n, xn, fixn, abs(fixn - xn)])
        while (1 - abs(max(self.get_phi_a, self.get_phi_b)) * (abs(fixn - xn)) >= self.e):
            xn = fixn 
            fixn = self.phi(xn)
            n += 1 
            self.table_simple_iteration_method.add_row([n, xn, fixn, abs(fixn - xn)])
        print(self.table_simple_iteration_method)

    def get_solve_simple_iteration_method_two_side(self):
        '''
        Двусторонняя сходимость
        '''
        n = 0
        xn = self.a 
        fixn = self.phi(xn)
        self.table_simple_iteration_method.add_row([n, xn, fixn, abs(fixn - xn)])
        while (abs(fixn - xn) >= self.e): 
            xn = fixn 
            fixn = self.phi(xn)
            n += 1 
            self.table_simple_iteration_method.add_row([n, xn, fixn, abs(fixn - xn)])
        print(self.table_simple_iteration_method)


        