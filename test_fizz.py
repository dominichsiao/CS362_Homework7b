import unittest
import fizz

class classTestFizz(unittest.TestCase):
    def test_Fizz_1(self):
        list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
        self.assertEqual(fizz.print_things(), list1)

    
    def test_Fizz_2(self):
        list2 = ['1', '2', '3', 'Fizz', '4', '5', '6', 'Fizz', '7', '8', '9', 'Fizz', '10', '11', '12', 'Fizz', '13', '14', '15', 'Fizz', '16', '17', '18', 'Fizz', '19', '20', '21', 'Fizz', '22', '23', '24', 'Fizz', '25', '26', '27', 'Fizz', '28', '29', '30', 'Fizz', '31', '32', '33', 'Fizz', '34', '35', '36', 'Fizz', '37', '38', '39', 'Fizz', '40', '41', '42', 'Fizz', '43', '44', '45', 'Fizz', '46', '47', '48', 'Fizz', '49', '50', '51', 'Fizz', '52', '53', '54', 'Fizz', '55', '56', '57', 'Fizz', '58', '59', '60', 'Fizz', '61', '62', '63', 'Fizz', '64', '65', '66', 'Fizz', '67', '68', '69', 'Fizz', '70', '71', '72', 'Fizz', '73', '74', '75', 'Fizz', '76', '77', '78', 'Fizz', '79', '80', '81', 'Fizz', '82', '83', '84', 'Fizz', '85', '86', '87', 'Fizz', '88', '89', '90', 'Fizz', '91', '92', '93', 'Fizz', '94', '95', '96', 'Fizz', '97', '98', '99', 'Fizz']
        self.assertEqual(fizz.print_things(), list2)


