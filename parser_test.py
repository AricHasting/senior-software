import unittest
import parser

class TestAvatar(unittest.TestCase):
  def test_no_avatar(self):
      self.assertEqual(parser.getAvatar('Hello'), False)

  def test_avatar(self):
    self.assertEqual(parser.getAvatar('/avatar Happy'), 'Happy')
  
  def test_with_whitespace(self):
    self.assertEqual(parser.getAvatar(' \t /avatar \t  \n Happy\n\t '), 'Happy')
  
  def test_empty(self):
    self.assertEqual(parser.getAvatar(''), False)
  
  def test_no_value(self):
    self.assertEqual(parser.getAvatar('/avatar'), '')

class TestCommand(unittest.TestCase):
  def test_no_command(self):
    self.assertEqual(parser.getCommand('This is a test!'), False)

  def test_command(self):
    self.assertEqual(parser.getCommand('/wizard'), 'wizard')
  
  def test_arguments(self):
    self.assertEqual(parser.getArguments('/connect 127.0.0.1 8080'), ['127.0.0.1', '8080'])

  def test_no_arguments(self):
    self.assertEqual(parser.getArguments('/connect'), [])
  
  def test_empty(self):
    self.assertEqual(parser.getCommand(''), False)
    self.assertEqual(parser.getArguments(''), [])

if __name__ == '__main__':
    unittest.main()