"""
This py contains the module 2 problems

This unittest is designed to ensure each problem is working
effectively as well as improve my ability to unittest, seeing as how
I have not made unittests in months the simplicity of the module 2
problems should suffice in re-learning.

To execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest Mod_2_and_3_prob/Module_2_Problems.py
    python -m unittest -k tests
"""

___author___ = "CW"
__version__ = "23/07/2025"

import unittest
from Module_2_Problems import module_2_problems

class TestModule2Problems(unittest.TestCase):
    def test_module_2_problems_define_print_statement(self):
        """
        Returns the designated accounts print statement in the form
        of a string.

        Args:
            name(string) = "Jo-Anne Sinclair"
            salary(int) = 1230393
        
        Returns:
            string: Name: Jo-Anne Sinclair
                    Salary: 123093
        """

        # Arrange, define variables
        name = "Jo-Anne Sinclair"
        salary = 1230393
        expected = (f"Name: {name}\nSalary: {salary:,.2f}")
        actual = f"Name: {name}\nSalary: {salary:,.2f}"
        
        # Act, run code your testing and assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()