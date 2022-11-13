from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
import sympy as sp
from ll3.views.SolveView import ViewSolvData

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
        self.table_combine_method.field_names = ['n', 'a', 'b', 'f(a)', 'f(b)', 'delta']

    def get_solv_combine_method_stationary_a(self):
        '''
        Неподвижна точка a 
        '''
        n = 0
        self.table_combine_method.add_row([n, self.a, self.b, self.f(self.a), self.f(self.b), abs(self.a - self.b)])
        while abs(self.a - self.b) > self.e:
            b1 = self.chordb(self.a, self.b)
            a1 = self.newton(self.b)
            self.a = a1
            self.b = b1
            n += 1
            self.table_combine_method.add_row([n, self.a, self.b, self.f(self.a), self.f(self.b), abs(self.a - self.b)])
        print(self.table_combine_method)

    def get_solv_combine_method_stationary_b(self):
        '''
        Неподвижна точка b
        '''
        n = 0
        self.table_combine_method.add_row([n, self.a, self.b, self.f(self.a), self.f(self.b), abs(self.a - self.b)])
        while abs(self.a - self.b) > self.e:
            a1 = self.chorda(self.a, self.b)
            b1 = self.newton(self.b)
            self.a = a1
            self.b = b1
            n += 1
            self.table_combine_method.add_row([n, self.a, self.b, self.f(self.a), self.f(self.b), abs(self.a - self.b)])
        print(self.table_combine_method)
