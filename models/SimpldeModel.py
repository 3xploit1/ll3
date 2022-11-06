from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
import sympy as sp
from views.SolveView import ViewSolvData

class SimpleMethod(ViewSolvData): 
    def __init__(self, e, a, b):
        super().__init__(e, a, b)    


    
    def get_info(self, f_a, f_a_derivative_2_order, f_b):
        try:
            if (f_a * f_a_derivative_2_order > 0): 
                print((f'Неподвижна в точке a =>  {Fore.GREEN}по недостатку методом касательной \n\t\t\t по избытку методом хорд{Style.RESET_ALL}'))
            elif (f_b * f_a_derivative_2_order > 0): 
                print(f'Неподвижна в точке b =>  {Fore.GREEN}по недостатку методом хорд \n\t\t\t по избытку методом касательных{Style.RESET_ALL}')     
            else: 
                raise    
        except: 
            print(f'{Fore.RED}Скрипт не может вернуть ответ{Style.RESET_ALL}')

    def set_table_simple_iteration_method(self):
        '''
        Создание объекта класса PrettyTable. Установление полей для таблицы 
        '''
        self.table_simple_iteration_method = PrettyTable()
        self.table_simple_iteration_method.field_names = [
            'iteration', 'x0', 'c', 'x1', 'z', 'r']
    
    def get_solv_simple_method(self):
        '''
        Суть метода - сужение интервала изоляции с двух сторон 
        
        На одной стороне сужение с помощью хорды на другой 
        с использованием касательной  
        
        Формулы  
        ======================================================
        Значение по недостатку --> метод касательных
        :`x1 = x0 - f(x0) / f'(x)`
        :Значение по избытку --> метод хорд
        :`z = c - f'(c) * (x0 - c) / (f(x0) - f(c))`      
        '''
        
        iteration = 1
        x0 = self.b
        c = self.a 
        r = 1 
        # if для a 
        while (self.e <= r):
            x1 = x0 - (5 * x0 - 8 * sp.ln(x0) - 8) / (5 - 8/x0) 
            z = c - (5 * c - 8 * sp.ln(c) - 8) * (x0-c) /  ((5 * x0 - 8 * sp.ln(x0) - 8) - (5 * c - 8 * sp.ln(c) - 8))
            r = abs(x1 - z) 
            x0 = x1
            c = z              
            self.table_combine_method.add_row([iteration, x0, c, x1, z, r])
            iteration += 1 
        #else 
            #while для b 
      
        print(self.table_simple_iteration_method)
        print(f'Ответ получен в {iteration - 1} итерации\nОтвет: {Fore.GREEN}{x1}{Style.RESET_ALL}')

        