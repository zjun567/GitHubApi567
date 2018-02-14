import unittest

from Api import result


class TestApi(unittest.TestCase):

    def testApi(self):
        self.assertEqual(result('zjun567')[1], ['GitHubApi567', 'Triangle567'])
        self.assertEqual(result('zjun567')[2], [4,6])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
