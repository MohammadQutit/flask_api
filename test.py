import unittest
import requests
from functions import memory_one,disk_one,cpu_one



class Test (unittest.TestCase):
    def test_cpu(self):
        x=requests.get("http://172.20.50.210:5000/cpu")
        self.assertEqual(200,x.status_code)

    def test_memory(self):
        x=requests.get("http://172.20.50.210:5000/memory")
        self.assertEqual(200,x.status_code)

    def test_disk(self):
        x=requests.get("http://172.20.50.210:5000/disk")
        self.assertEqual(200,x.status_code)

    def test_cpu_now(self):
        self.assertIsNotNone(cpu_one())

        

if __name__=="__main__":
    unittest.main()