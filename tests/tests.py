import unittest
import sys
sys.path.append(".")
import json
from init import create_app

test_app = create_app()

class TestCardMethods(unittest.TestCase):

    def test_get_by_name(self):
        response = json.loads(test_app.test_client().get("/cards/Snivy").data)
        
        expected = [{
            "card_id": 4,
            "card_name": "Snivy",
            "hp": 60,
            "price": 1.9,
            "retreat_cost": 1,
            "stage": 0
        }]
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()