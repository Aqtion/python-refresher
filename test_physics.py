import physics
import unittest


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(50, 1000), 490500)
        self.assertEqual(physics.calculate_buoyancy(37, 526), 190922.22)
        self.assertNotEqual(physics.calculate_buoyancy(5, 20), 200)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(50, 50), True)
        self.assertEqual(physics.will_it_float(3, 10000), False)
        self.assertNotEqual(physics.will_it_float(6, 10000), True)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(10), 98100)
        self.assertEqual(physics.calculate_pressure(35), 343350)
        self.assertNotEqual(physics.calculate_pressure(72), 706319)


if __name__ == "__main__":
    unittest.main()
