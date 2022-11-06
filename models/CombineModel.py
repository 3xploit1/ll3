from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
import sympy as sp
from views.SolveView import ViewSolvData

class CombineMethod(ViewSolvData): 
    def __init__(self, e, a, b):
        super().__init__(e, a, b)    
    
    def get_info(self, f_a, f_a_derivative_2_order, f_b):
        try:
            if (f_a * f_a_derivative_2_order > 0): 
                print((f'Неподвижна в точке a =>  {Fore.GREEN}по недостатку методом касательной \n\t\t\t по избытку методом хорд{Style.RESET_ALL}'))
                return 'a'
            elif (f_b * f_a_derivative_2_order > 0): 
                print(f'Неподвижна в точке b =>  {Fore.GREEN}по недостатку методом хорд \n\t\t\t по избытку методом касательных{Style.RESET_ALL}')     
                return 'b'
            else: 
                raise    
        except: 
            print(f'{Fore.RED}Скрипт не может вернуть ответ{Style.RESET_ALL}')

    def set_table_combine_method(self):
        '''
        Создание объекта класса PrettyTable. Установление полей для таблицы 

        :`x0` - начальная точка для касательной
        :`c` - начальная точка для хорды
        :`x1` - точка пересечения касательной и оси x 
        :`z` - точка пересечения хорды и оси x
        :`r` - итерационная разность
        '''
        self.table_combine_method = PrettyTable()
        self.table_combine_method.field_names = ['iteration', 'x0', 'c', 'x1', 'z', 'r']            
    
    def get_solv_combine_method_stationary_a(self):
        '''
        Неподвижна точка a 
        '''
        iteration = 1
        x0 = self.a
        c = self.b 
        r = 1 
        while (self.e <= r):
            x1 = x0 - (self.f(x0)) / (5 - 8 / x0)
            z = c - (self.f(c)) * (c - x0) / ((self.f(x0)) - (self.f(c)))
            r = abs(x1 - z) 
            x0 = x1
            c = z              
            self.table_combine_method.add_row([iteration, x0, c, x1, z, r])
            iteration += 1
            
        print(self.table_combine_method)
        print(f'Ответ: {Fore.GREEN}{x1}{Style.RESET_ALL}')

    def get_solv_combine_method_stationary_b(self):
        '''
        Неподвижна точка b
        '''
        iteration = 1
        x0 = self.b
        c = self.a 
        r = 1 
        while (self.e <= r):
            x1 = x0 - ((self.f(x0)) / (5 - 8 / x0)) # хорда 
            z = c - (self.f(c)) * (x0 - c) / (self.f(x0) - self.f(c)) # касательная
            r = abs(x1 - z) 
            x0 = x1
            c = z              
            self.table_combine_method.add_row([iteration, x0, c, x1, z, r])
            iteration += 1    

        print(self.table_combine_method)
        print(f'Ответ получен в {iteration - 1} итерации\nОтвет: {Fore.GREEN}{x1}{Style.RESET_ALL}')

        