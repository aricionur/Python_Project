import unittest
from Codility_bucket_problem.source.Color import Color

class TestForColorClass(unittest.TestCase):


    def test_init(self):
        color_id = 1
        new_color = Color(color_id)

        self.assertTrue(new_color.id == color_id)
        self.assertTrue(new_color.counter == 1)
        pass

    def test_eq_input_integer(self):
        color_id = 1
        new_color = Color(color_id)
        test_integer = color_id
        returned_bolean = False

        if new_color == test_integer:
            returned_bolean = True

        self.assertTrue(returned_bolean == True)

        pass

    def test_eq_input_Color(self):
        color_id = 1
        new_color_1 = Color(color_id)
        new_color_2 = Color(color_id)
        returned_boolean = False

        if new_color_1 == new_color_2:
            returned_boolean = True

        self.assertTrue(returned_boolean == True)
        pass

    def test_increaese_counter(self):

        color_id = 1
        new_color = Color(color_id)
        increase_amount = 1
        initial_counter = new_color.counter

        new_color.increase_counter()
        self.assertEqual(new_color.counter, 2)
        increased_counter = new_color.counter
        expected_counter = initial_counter + increase_amount

        self.assertTrue(increased_counter == expected_counter)
        pass



