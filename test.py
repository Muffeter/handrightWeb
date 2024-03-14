import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/generate'

    def test_generate_with_params(self):
        params = {
            'line_spacing': 100,
            'fill': 255,
            'left_margin': 20,
            'top_margin': 10,
            'right_margin': 20,
            'bottom_margin': 10,
            'word_spacing': -5,
            'line_spacing_sigma': 2,
            'font_size_sigma': 2,
            'word_spacing_sigma': 2,
            'start_chars': '“（[<',
            'end_chars': '，。',
            'perturb_x_sigma': 2,
            'perturb_y_sigma': 2,
            'perturb_theta_sigma': 0.1
        }

        response = requests.get(self.BASE_URL, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Generated with parameters')

    def test_generate_without_params(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Generated with parameters')

if __name__ == '__main__':
    unittest.main()
