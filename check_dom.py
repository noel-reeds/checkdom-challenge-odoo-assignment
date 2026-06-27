from typing import Tuple

class _Soln:
    def check_dom(self, str_param: str) -> Tuple[bool, str]:
        """
        Check if an HMTL tag is valid or not.
        Args:
            str_param(str): An input HTML string containing tags.
        Return:
            bool or str: Return False if HTML tags are mismatched or invalid
                        Returns mismatched tag if there's only one.
                        Returns True if all tags are matched and valid.
        Examples:
            >>> check_dom("<p>Hello World!</p>")
            True
            
            >>> check_dom("<p>Hello World!</i>")
            'p'

            >>> check_dom("<p>Hello World!")
            False

        HTML Tags to be used:
            The elements that will be used are: <b>, <i>, <em>, <div>, <p>
        """
        tags = ('<b>', '<i>', '<em>', '<div>', '<p>')
        mismatched_t = []
        matched_t = []

        # number of tags should be even, odd number of tags
        # implies invalid tags.
        if str_param.count('<') % 2 != 0 or str_param.count('>') % 2 != 0:
            return False
        if str_param.count('<') != str_param.count('>'):
            return False
        for k in tags:
            m = k[:1] + '/' + k[1:]
            if k in str_param and m in str_param:
                matched_t.append(k)
            elif k in str_param and m not in str_param:
                mismatched_t.append(k)
        # check if all tags are matched and return True
        if len(mismatched_t) == 0 and len(matched_t) >= 1:
            return True
        # return False for more than one mismatch tags
        if len(mismatched_t) == 1:
            return mismatched_t[0].strip('<>')
        else:
            return False

import inspect
from inspect import signature
from unittest import TestCase
class check_dom_test_case(TestCase):
    
    def test_check_dom_cls_fn(self):
        self.assertTrue(('__class__', _Soln) in 
                inspect.getmembers(_Soln()))
        with self.assertRaises(AssertionError):
            self.assertTrue(('check_dom', _Soln().check_dom) in
                    inspect.getmembers(_Soln()))
    
    def test_check_dom_objects(self):
        self.assertTrue(inspect.isclass(_Soln))
        self.assertTrue(inspect.ismethod(_Soln().check_dom))

    def test_check_dom_args(self):
        self.assertTrue(inspect.isfunction(_Soln.check_dom))
        self.assertIn('str_param', signature(_Soln.check_dom).parameters)

    def test_check_dom_annotations(self):
        self.assertIs(signature(
                _Soln.check_dom).parameters['str_param'].annotation, str)
        self.assertIs(signature(
                _Soln.check_dom).return_annotation, Tuple[bool, str])

    def test_valid_html_str(self):
        self.assertTrue(
                _Soln().check_dom('<div><b><p>hello world</p></b></div>'))
        self.assertTrue(_Soln().check_dom('<p>Hello World!</p>'))

    def test_html_str_one_mismatched_tag(self):
        self.assertEqual('b',
                _Soln().check_dom('<div><b><p>hello world</p></i></div>'))
        self.assertEqual('div',
                _Soln().check_dom('<div><b><p>hello world</p></b></em>'))

    def test_html_str_several_mismatched_tags(self):
        self.assertFalse(
                _Soln().check_dom('<div><b><p>hello world</p></i></i>'))
        self.assertFalse(
                _Soln().check_dom('<em><i><p>hello world</p></b></div>'))

    def test_invalid_html_str(self):
        self.assertFalse(_Soln().check_dom('<p>Hello World!'))
        self.assertFalse(_Soln().check_dom('Hello World!</em>'))
