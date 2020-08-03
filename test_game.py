import unittest

from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_x = 1
        self.player_y = 2
        self.map = 'Map'
        self._get_room = (0,0)
        self.current_room = self._get_room

    def test_x_check(self):
        expected = 0
        result = self.player_x
        return self.assertNotEqual(expected,result)

    def test_move_false(self):
        return self.assertIsNot(self.map, self._get_room)

    def test_coords(self):
        return self.assertIsNotNone(self.map)

    def test_get_room(self):
        return self.assertIs(self._get_room,self.current_room)

    def test_greater(self):
        return self.assertLess(self.player_x,self.player_y)

    def test_False(self):
        return self.assertTrue(self.player_x)





if __name__ == '__main__':
    unittest.main()
