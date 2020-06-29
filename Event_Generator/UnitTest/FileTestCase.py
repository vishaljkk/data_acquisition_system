import unittest

class TestDetection(unittest.TestCase): 
	def test_detection(self):
		fileName = 'myfile.pdf'
		print("File Extension:",fileName[-3:])
		self.assertEqual(fileName[-3:], 'txt',f'File type is {fileName[-3:]} rather than txt')

if __name__ == '__main__': 
	unittest.main()