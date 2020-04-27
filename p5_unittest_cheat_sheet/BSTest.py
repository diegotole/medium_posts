import mock
import unittest
from unittest import TestCase

from p5_unittest_cheat_sheet.guinea_pig_module import guinea_pig


@mock.patch("guinea_pig_module.requests.post")
@mock.patch("guinea_pig_module.requests.get")
@mock.patch("guinea_pig_module.calculate_avg")
class TestingGuineaPig(TestCase):

    def test_good_run(self, mock_avg, mock_get, mock_post):
        resp = mock.Mock()
        resp.json.return_value = [
            [1, "a", 33],
            [2, "b", -1],

        ]

        mock_get.return_value = resp

        r = guinea_pig("", "")

        self.assertTrue(r)

    def test_bad_run_timeout(self, mock_avg, mock_get, mock_post):
        mock_get.side_effect = TimeoutError("Bad things happened")
        r = guinea_pig("", "")
        self.assertFalse(r)

    def test_json_exception(self, mock_avg, mock_get, mock_post):
        resp = mock.Mock()
        resp.json.side_effect = Exception("something weird while parsing json")

        mock_get.return_value = resp
        r = guinea_pig("", "")

        self.assertFalse(r)


# class MyTestCase(TestCase):
#
#     def not_a_test(self):
#         pass
#
#     @mock.patch()
#     def test_something(self):
#         # run your function here
#         # evaluate test result
#         flag = True
#         self.assertEqual(True, flag)
#
#     def test_something_else(self):
#         self.assertEqual(True, False)
#
#
#     @mock.patch("guinea_pig_module.request.post")
#     @mock.patch("guinea_pig_module.request.get")
#     @mock.patch("guinea_pig_module.calculate_avg")
#     def test_get_sum(self, mocked_calculate_avg, mocked_get, mocked_post):
#         pass
#
#
#
#     @mock.patch("guinea_pig_module.calculate_avg")
#     def test_get_sum(self, mocked_calculate_avg):
#
#         #every call to calculate_avg inside guinea pig module will
#         #return a Mock() object.
#         #if you do not need to do anything with the response, do not bother
#         #with any extra steps
#
#         #if your code needs a number in order to continue execution
#         mocked_calculate_avg.return_value = 3
#         #for a hard coded list
#         mocked_calculate_avg.return_value = [1,2,3]
#
#         #for a different value on every call, use this instead
#         #this will return 1, than 2 on 2nd call, and 3 in the 3rd calls
#         mocked_calculate_avg.side_effect = [1,2,3]
#
#         #for dynamic response, use lambda
#         #this will return always the double
#         mocked_calculate_avg.side_effect = lambda x: x*2
#
#         #if you were reading inside a loop
#         #and want to be memory efficient
#         def myGen():
#           for i in range(1000000):
#               yield i
#
#         mocked_calculate_avg.side_effect =  myGen
#         #use like this:
#         #for n in mocked_calculate_avg():
#         #      print(n)


if __name__ == '__main__':
    unittest.main()
