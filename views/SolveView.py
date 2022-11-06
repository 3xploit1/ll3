from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
from models.AbstractModel import *

class ViewSolvData(AbstractSolver):

    def get_start_data(self):
        '''
        Вывод входных данных
        '''
        print(f"\n{Fore.RED}Уравнение{Style.RESET_ALL}:    5 * x - 8 * ln(x) - 8 = 0")
        print(f"{Fore.RED}Погрешность{Style.RESET_ALL}:  {self.e} ")
        print(f"{Fore.RED}Интервал{Style.RESET_ALL}:     [{self.a} ; {self.b}] {Style.RESET_ALL}\n")

    def get_about_combine_method(self):
        print(f"{Fore.GREEN}----------------------------------------{Style.RESET_ALL}")
        print('Комбинированный метод')
        print(f"{Fore.GREEN}----------------------------------------{Style.RESET_ALL}")

    def get_about_simple_iteration_method(self):
        print(f"{Fore.GREEN}----------------------------------------{Style.RESET_ALL}")
        print('Метод простой итерации\n')
        print(f"{Fore.GREEN}----------------------------------------{Style.RESET_ALL}\n")

    def get_print_combine_method(self,
                                 derivative_f,
                                 derivative_f_2_order,
                                 f_a,
                                 f_b,
                                 f_a_derivative,
                                 f_b_derivative,
                                 f_a_derivative_2_order,
                                 f_b_derivative_2_order):

        print(f"f`(x) = {derivative_f}\n"
              f"f``(x) = {derivative_f_2_order}\n"
              f"f(a) = {f_a}\n"
              f"f(b) = {f_b}\n"
              f"f`(a) = {f_a_derivative}\n"
              f"f`(b) = {f_b_derivative}\n"
              f"f``(a) = {f_a_derivative_2_order}\n"
              f"f``(b) = {f_b_derivative_2_order}\n")
    
