from django.test import TestCase


class SampleTestCase(TestCase):
    def test_two_plus_two(self):
        self.assertEqual(2+2, 4)

    def test_nine_minus_three(self):
        self.assertEqual(9-3, 6)