# -*- coding: utf-8 -*-
import unittest
from sistema_mobilidade import Bicicleta, Usuario

class TestBicicleta(unittest.TestCase):

    def test_bicicleta_inicializacao(self):
        """Testa se a bicicleta inicializa corretamente com seus atributos protegidos."""
        bike = Bicicleta("BK-100", "Urbana", 85.0)
        self.assertEqual(bike.codigo, "BK-100")
        self.assertEqual(bike.modelo, "Urbana")
        self.assertEqual(bike.carga_bateria, 85.0)
        self.assertTrue(bike.disponivel)

    def test_bicicleta_carga_bateria_valida(self):
        """Testa se o setter de bateria aceita valores válidos nos limites."""
        bike = Bicicleta("BK-100", "Urbana")
        
        bike.carga_bateria = 100.0
        self.assertEqual(bike.carga_bateria, 100.0)
        
        bike.carga_bateria = 0.0
        self.assertEqual(bike.carga_bateria, 0.0)
        
        bike.carga_bateria = 50.5
        self.assertEqual(bike.carga_bateria, 50.5)

    def test_bicicleta_carga_bateria_invalida_superior(self):
        """Testa se o setter de bateria levanta ValueError para valores acima de 100%."""
        bike = Bicicleta("BK-100", "Urbana")
        with self.assertRaises(ValueError):
            bike.carga_bateria = 101.0

    def test_bicicleta_carga_bateria_invalida_inferior(self):
        """Testa se o setter de bateria levanta ValueError para valores negativos."""
        bike = Bicicleta("BK-100", "Urbana")
        with self.assertRaises(ValueError):
            bike.carga_bateria = -5.0

    def test_bicicleta_usar_consumo_normal(self):
        """Testa se o método usar reduz a bateria proporcionalmente (0.5% por minuto)."""
        bike = Bicicleta("BK-100", "Urbana", 100.0)
        bike.usar(20)  # 20 * 0.5 = 10% de consumo
        self.assertEqual(bike.carga_bateria, 90.0)
        self.assertTrue(bike.disponivel)

    def test_bicicleta_usar_bateria_zerada(self):
        """Testa se a bateria zera e a bicicleta fica indisponível se exceder o tempo."""
        bike = Bicicleta("BK-100", "Urbana", 10.0)
        bike.usar(30)  # 30 * 0.5 = 15% de consumo (deve zerar e desativar)
        self.assertEqual(bike.carga_bateria, 0.0)
        self.assertFalse(bike.disponivel)

    def test_bicicleta_recarregar(self):
        """Testa se recarregar restaura bateria e disponibilidade."""
        bike = Bicicleta("BK-100", "Urbana", 0.0, disponivel=False)
        bike.recarregar()
        self.assertEqual(bike.carga_bateria, 100.0)
        self.assertTrue(bike.disponivel)

    def test_bicicleta_autonomia(self):
        """Testa se o cálculo de autonomia está correto (0.8km por 1%)."""
        bike = Bicicleta("BK-100", "Urbana", 50.0)
        self.assertEqual(bike.autonomia_estimada(), 40.0)  # 50.0 * 0.8

    def test_bicicleta_str_representacao(self):
        """Testa se o dunder método __str__ retorna a representação esperada."""
        bike = Bicicleta("BK-100", "Urbana", 100.0)
        self.assertEqual(str(bike), "Bicicleta BK-100 (Urbana) - Bateria: 100.0% - Status: Disponível")


class TestUsuario(unittest.TestCase):

    def test_usuario_inicializacao(self):
        """Testa se o usuário inicializa corretamente e previne saldo negativo no construtor."""
        user = Usuario("Alice", 20.0)
        self.assertEqual(user.nome, "Alice")
        self.assertEqual(user.saldo, 20.0)
        self.assertIsNone(user.bike_alugada)
        self.assertEqual(user.viagens_realizadas, 0)

        # Testando sanitização de saldo negativo no construtor
        user_neg = Usuario("Bob", -10.0)
        self.assertEqual(user_neg.saldo, 0.0)  # max(0.0, -10.0) -> 0.0

    def test_usuario_setter_saldo_negativo(self):
        """Testa se o setter de saldo limita valores negativos a 0.0."""
        user = Usuario("Alice", 20.0)
        user.saldo = -15.0
        self.assertEqual(user.saldo, 0.0)

    def test_usuario_adicionar_saldo(self):
        """Testa se o depósito incrementa o saldo através do setter."""
        user = Usuario("Alice", 10.0)
        user.adicionar_saldo(15.5)
        self.assertEqual(user.saldo, 25.5)

    def test_usuario_adicionar_saldo_invalido(self):
        """Testa se depósitos de valores negativos levantam ValueError."""
        user = Usuario("Alice", 10.0)
        with self.assertRaises(ValueError):
            user.adicionar_saldo(-5.0)


class TestIntegracaoSistema(unittest.TestCase):

    def test_aluguel_sucesso(self):
        """Testa fluxo feliz de aluguel de bicicleta."""
        user = Usuario("Alice", 10.0)
        bike = Bicicleta("BK-100", "Urbana", 100.0)
        
        resultado = user.alugar_bike(bike)
        
        self.assertEqual(resultado, "Aluguel realizado com sucesso!")
        self.assertEqual(user.bike_alugada, bike)
        self.assertFalse(bike.disponivel)

    def test_aluguel_falha_ja_alugada(self):
        """Testa se o usuário é impedido de alugar duas bicicletas ao mesmo tempo."""
        user = Usuario("Alice", 20.0)
        bike1 = Bicicleta("BK-1", "Urbana")
        bike2 = Bicicleta("BK-2", "Urbana")
        
        user.alugar_bike(bike1)
        resultado = user.alugar_bike(bike2)
        
        self.assertEqual(resultado, "Erro: Usuário já possui uma bicicleta alugada.")
        self.assertEqual(user.bike_alugada, bike1)

    def test_aluguel_falha_saldo_insuficiente(self):
        """Testa se o aluguel é negado caso o usuário tenha menos que R$ 5,00."""
        user = Usuario("Alice", 4.99)
        bike = Bicicleta("BK-100", "Urbana")
        
        resultado = user.alugar_bike(bike)
        
        self.assertEqual(resultado, "Erro: Saldo mínimo de R$ 5,00 necessário para aluguel.")
        self.assertIsNone(user.bike_alugada)

    def test_aluguel_falha_bike_indisponivel(self):
        """Testa se o aluguel é negado se a bicicleta já estiver em uso."""
        user = Usuario("Alice", 10.0)
        bike = Bicicleta("BK-100", "Urbana", disponivel=False)
        
        resultado = user.alugar_bike(bike)
        
        self.assertEqual(resultado, "Erro: Bicicleta não está disponível.")
        self.assertIsNone(user.bike_alugada)

    def test_aluguel_falha_bateria_baixa(self):
        """Testa se o aluguel é negado se a bateria estiver em 10% ou menos."""
        user = Usuario("Alice", 10.0)
        bike = Bicicleta("BK-100", "Urbana", carga_bateria=10.0)
        
        resultado = user.alugar_bike(bike)
        
        self.assertEqual(resultado, "Erro: Carga de bateria insuficiente (mínimo de 10%).")
        self.assertIsNone(user.bike_alugada)

    def test_devolucao_sucesso(self):
        """Testa a devolução, cálculo de custo, dedução de bateria e saldo, e liberação da bike."""
        user = Usuario("Alice", 15.0)
        bike = Bicicleta("BK-100", "Urbana", 80.0)
        
        user.alugar_bike(bike)
        
        # 20 minutos de viagem. 
        # Custo: 20 * 0.40 = R$ 8.00. Saldo restante: 15.00 - 8.00 = R$ 7.00
        # Consumo bateria: 20 * 0.5 = 10%. Bateria restante: 80% - 10% = 70%
        resultado = user.devolver_bike(20)
        
        self.assertIn("Devolução realizada!", resultado)
        self.assertIn("Custo da corrida: R$ 8.00", resultado)
        self.assertIn("Saldo restante: R$ 7.00", resultado)
        
        self.assertIsNone(user.bike_alugada)
        self.assertEqual(user.saldo, 7.0)
        self.assertEqual(user.viagens_realizadas, 1)
        
        self.assertEqual(bike.carga_bateria, 70.0)
        self.assertTrue(bike.disponivel)

    def test_devolucao_saldo_zerado(self):
        """Testa se o saldo é debitado e zerado, mas não fica negativo (garantido pelo setter)."""
        user = Usuario("Alice", 5.0)
        bike = Bicicleta("BK-100", "Urbana", 100.0)
        
        user.alugar_bike(bike)
        
        # 20 minutos custa R$ 8.00. Como só tem R$ 5.00, o saldo deve zerar (5.0 - 8.0 = -3.0 -> setter corrige para 0.0)
        user.devolver_bike(20)
        
        self.assertEqual(user.saldo, 0.0)

    def test_devolucao_bike_bateria_esgotada(self):
        """Testa se na devolução, se a bateria zerar, a bicicleta fica indisponível para novos aluguéis."""
        user = Usuario("Alice", 20.0)
        bike = Bicicleta("BK-100", "Urbana", 15.0)  # Carga acima de 10.0 para poder alugar
        
        user.alugar_bike(bike)
        
        # 30 minutos de viagem consome 15% de bateria (zera bateria da bike)
        user.devolver_bike(30)
        
        self.assertEqual(bike.carga_bateria, 0.0)
        self.assertFalse(bike.disponivel)  # Fica indisponível até ser recarregada


if __name__ == "__main__":
    unittest.main()
