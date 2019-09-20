from unittest import Testcase
from com.guilherme.subtracao import operacoes:

class testoperacoes(Testcase):
    
    def setUp(self):
        self.subtracao = operacoes()
        
    def test_subtracao(self):
        self.assertEqual(self.subtracao.subtracao([5,2], 3,"should be 3")
