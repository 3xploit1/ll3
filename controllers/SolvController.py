import sys
sys.path.append("")
from ll3.models.CombineModel import CombineMethod
from ll3.models.SimpldeModel import SimpleMethod

class SolvControll(CombineMethod, SimpleMethod):
    def set_data_combine_method(self):
        data = self.get_solv()
        self.get_print_combine_method(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        self.set_table_combine_method()
        
        if (self.get_info(data[2], data[6], data[3]) == 'a'): 
            self.get_solv_combine_method_stationary_a()
        else: 
            self.get_solv_combine_method_stationary_b()
        return self 
        
    def get_data_combine_method(self):
        self.get_about_combine_method()
        self.get_start_data()
        return self

    def set_data_simple_iteration_method(self):
        data = self.get_solv()
        self.get_print_combine_method(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        self.set_table_simple_iteration_method()
        self.get_print_const()
        self.simp_solv()
        # self.get_print_fi_a()
        # self.get_print_fi_b()
        # self.check_convergence()
        return self

    def get_data_simple_iteration_method(self): 
        self.get_about_simple_iteration_method()
        self.get_start_data()
        return self

if __name__ == "__main__":
    solv = SolvControll(0.00001, 3.0, 3.9)
    # solv.get_data_combine_method().set_data_combine_method()
    solv.get_data_simple_iteration_method().set_data_simple_iteration_method()

