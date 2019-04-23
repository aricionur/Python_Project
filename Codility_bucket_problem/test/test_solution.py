import unittest
from Codility_bucket_problem.source.Solution import solution


class UnitTestForBucket(unittest.TestCase):

    def setUp(self):
        self.solution = solution
        pass

    def test_one_ball_one_bucket(self):
        N = 1
        Q = 1
        B = [0]
        C = [0]

        result = self.solution(N, Q, B, C)

        self.assertTrue(result, 1)
        pass

    def test_multi_balls_one_bucket(self):
        N = 1
        Q = 2
        B = [0, 0, 0, 0]
        C = [0, 1, 0, 2]

        result = self.solution(N, Q, B, C)

        self.assertTrue(result, 2)
        pass

    def test_multi_balls_multi_buckets(self):
        N = 3
        Q = 2
        B = [0, 1, 2, 0, 2, 1, 0]
        C = [7, 1, 0, 7, 3, 4, 7]

        result = self.solution(N, Q, B, C)

        self.assertTrue(result, 7)
        pass

    def test_one_occurrence(self):
        N = 3
        Q = 1
        B = [2, 1, 2, 0, 2, 1, 0]
        C = [0, 1, 0, 7, 3, 4, 7]

        result = self.solution(N, Q, B, C)

        self.assertTrue(result, 1)
        pass

    def test_none_occurrence(self):
        N = 3
        Q = 2
        B = [2, 1, 2, 0, 2, 1, 0]
        C = [0, 1, 0, 7, 3, 4, 7]

        result = self.solution(N, Q, B, C)

        self.assertTrue(result, -1)
        pass

if __name__ == '__main__':
    unittest.main()