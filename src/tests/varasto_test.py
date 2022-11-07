import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_konstruktorissa_nollataan(self):
        invalid = Varasto(-10)
        self.assertAlmostEqual(invalid.tilavuus, 0.0)

    def test_negatiivinen_saldo_konstruktorissa_nollataan(self):
        invalid = Varasto(1.0, -1.0)
        self.assertAlmostEqual(invalid.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_muuta_tilaa(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo_ennen)

    def test_saldon_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        # varmistetaan, ettei saldo ole muutenkin nolla
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_saldon_ylittavan_maaran_ottaminen_palauttaa_saldon(self):
        # varasto luotiin saldolla nolla
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_merkkijono_muodostuu_oikein(self):
        self.varasto.lisaa_varastoon(3) # saldo on nyt 3
        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")