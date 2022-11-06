from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
import sympy as sp
from views.SolveView import ViewSolvData

class SimpleMethod(ViewSolvData): 
    def __init__(self, e, a, b):
        super().__init__(e, a, b)    


    def set_table_simple_iteration_method(self):
        '''
        Создание объекта класса PrettyTable. Установление полей для таблицы 
        '''
        self.table_simple_iteration_method = PrettyTable()
        self.table_simple_iteration_method.field_names = [
            'iteration', 'x0', 'c', 'x1', 'z', 'r']
    
    def get_canonical_view(self): 
        '''
        Преобразование к каноническому виду
        '''
        ...
    
    def check_convergence(self): 
        '''
        Проверка на сходимость 
        '''
        ...
    
    def get_solve_simple_iteration_method(self): 
        '''
        Процесс итерации 
        '''
        ...


        