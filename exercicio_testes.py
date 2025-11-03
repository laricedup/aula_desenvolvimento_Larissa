import unittest


class TestesExemplos(unittest.TestCase):
    def testar_numero_maior_10(self):
        numero= 12
        self.assertTrue(numero>10)




    def testar_numero_menor_10(self):
        numero_menor= 7
        self.assertTrue(numero_menor<10)



    def testarVogal(self):
     vogais = ("a", "e", "i", "o", "u")
     letra = 'e'
     self.assertTrue(letra in vogais)

if __name__ == "__main__":
    unittest.main()
       
