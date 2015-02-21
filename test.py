from zombie import zombie
import unittest

class TestmainFunction(unittest.TestCase):
	def setUp(self):
		self.z = zombie((1,1))
		print 'I am setUp'

	def tearDown(self):
		self.z = None
		print 'I am tearDown'

	def test_up(self):
		self.z.up()
		t = zombie((1,0))
		self.assertEqual(self.z.current_position, t.current_position)
		print 'I am test_do_something'

	def test_do_something_else(self):
		print 'I am test_do_something_else'

if __name__ == '__main__':
	unittest.main()
