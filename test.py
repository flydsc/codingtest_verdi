from zombie import zombie
from creature import Creature
from main import control
import unittest
import numpy as np

class TestmainFunction(unittest.TestCase):
	def setUp(self):
		self.dimension = 4
		self.z = zombie((1,1))
		self.c = Creature((1,2))
		self.poors_positions = [(0,0),(2,2),(0,2)]
		self.grid = np.zeros((4,4))
		self.moves = "LURRDD"
		self.scores = 0

	def tearDown(self):
		self.z = None

	def test_up(self):
		self.z.up()
		t = zombie((1,0))
		self.assertEqual(self.z.current_position, t.current_position)
		t = None


	def test_down(self):
		self.z.down()
		t = zombie((1,2))
		self.assertEqual(self.z.current_position, t.current_position)
		t = None

	def test_left(self):
		self.z.left()
		t = zombie((0,1))
		self.assertEqual(self.z.current_position, t.current_position)
		t = None


	def test_right(self):
		self.z.right()
		t = zombie((2,1))
		self.assertEqual(self.z.current_position, t.current_position)
		t = None

	def test_move(self):
		self.z.move(self.moves,self.grid)
		self.assertEqual(self.z.scores, self.scores)

	def test_c_Constructor(self):
		self.assertEqual(self.c.current_position,(2,1))

	def test_go(self):
		c = control(self.dimension,self.moves,(1,1),self.poors_positions)
		c.go()
		self.assertEqual(c.Zombie.scores, 2)


if __name__ == '__main__':
	unittest.main()
