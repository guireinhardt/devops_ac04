from unittest import TestCase
from com.guilherme.subtracao import operacoes

class testoperacoes(TestCase):
    
    def setUp(self):
        self.subtracao = operacoes()
        
    def test_subtracao(self):
        self.assertEqual(self.subtracao.subtracao([5,2]), 3,"should be 3")