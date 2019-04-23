import unittest
from Codility_bucket_problem.source.Bucket import Bucket
from Codility_bucket_problem.source.Color import Color

class TestForBucketClass(unittest.TestCase):

    def setUp(self):

        pass

    def test_init(self):
        bucket_id = 1
        bucket = Bucket(bucket_id)

        self.assertTrue(bucket.id == bucket_id)
        self.assertTrue((hasattr(bucket, 'color_list')))
        #self.assertTrue(type(bucket.color_list) == type(list()))
        pass

    def test_add_color_return(self):
        color_id = 2
        bucket_id = 1
        new_color = Color(color_id)
        new_bucket = Bucket(bucket_id)

        returned_color = new_bucket.add_color(color_id)

        self.assertTrue(color_id == returned_color.id)
        pass

    def test_appendig_color_list(self):
        color_id = 2
        bucket_id = 1
        new_color = Color(color_id)
        new_bucket = Bucket(bucket_id)

        new_bucket.add_color(color_id)
        color_list_first_element = new_bucket.color_list[0]

        self.assertTrue(color_id == color_list_first_element.id)
        self.assertEqual(len(new_bucket.color_list), 1)
        self.assertIsInstance(color_list_first_element, Color)
        pass

if __name__ == '__main__':
    unittest.main()