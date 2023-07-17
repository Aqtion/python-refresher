import physics
import unittest
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(50, 1000), 490500)
        self.assertEqual(physics.calculate_buoyancy(37, 526), 190922.22)
        self.assertNotEqual(physics.calculate_buoyancy(5, 20), 200)

        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(-1, -1)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(50, 50), True)
        self.assertEqual(physics.will_it_float(3, 10000), False)
        self.assertNotEqual(physics.will_it_float(6, 10000), True)

        with self.assertRaises(ValueError):
            physics.will_it_float(-1, -1)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(10), 199425)
        self.assertEqual(physics.calculate_pressure(35), 444675)
        self.assertNotEqual(physics.calculate_pressure(72), 706319)

        with self.assertRaises(ValueError):
            physics.calculate_pressure(-1)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(100, 10), 10)
        self.assertNotEqual(physics.calculate_acceleration(150, 30), 6)

        with self.assertRaises(ValueError):
            physics.calculate_acceleration(50, -3)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(50, 25), 2)
        self.assertNotEqual(physics.calculate_angular_acceleration(60, 30), 3)

        with self.assertRaises(ValueError):
            physics.calculate_angular_acceleration(30, -3)

    def test_calculate_torque(self):
        self.assertEqual(round(physics.calculate_torque(30, 45, 5), 3), 106.066)
        self.assertNotEqual(physics.calculate_torque(60, 30, 4), 100)

        with self.assertRaises(ValueError):
            physics.calculate_torque(-50, -3, 3)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(4, 4), 64)
        self.assertNotEqual(physics.calculate_moment_of_inertia(6, 4), 200)

        with self.assertRaises(ValueError):
            physics.calculate_moment_of_inertia(-30, -3)

    def test_calculate_auv_acceleration(self):
        self.assertAlmostEqual(
            physics.calculate_auv_acceleration(30, 5)[0] * 100, 29.8858409427
        )
        self.assertAlmostEqual(
            physics.calculate_auv_acceleration(30, 5)[1] * 100, 2.614672282429
        )
        self.assertNotAlmostEqual(
            physics.calculate_auv_acceleration(40, 8)[0] * 100, 35
        )
        self.assertNotAlmostEqual(
            physics.calculate_auv_acceleration(40, 8)[0] * 100, 39
        )

        with self.assertRaises(ValueError):
            physics.calculate_auv_acceleration(-30, -3)

    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(round(physics.calculate_auv_angular_acceleration(60, 30)), 15)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(70, 3), 11)

        with self.assertRaises(ValueError):
            physics.calculate_auv_angular_acceleration(-30, -3)

    def test_calculate_auv2_acceleration(self):
        self.assertTrue(
            np.allclose(
                physics.calculate_auv2_acceleration(
                    [2, 4, 8, 6], np.pi / 4, np.pi / 6, 1
                ),
                [np.sqrt(2) - 2 * np.sqrt(6), -2 * np.sqrt(2) - np.sqrt(6)],
            )
        )
        self.assertFalse(
            np.allclose(
                physics.calculate_auv2_acceleration(
                    [2, 4, 5, 3], np.pi / 6, np.pi / 4, 1
                ),
                [np.sqrt(5) - 3 * np.sqrt(8), -2 * np.sqrt(3) - np.sqrt(7)],
            )
        )
        with self.assertRaises(ValueError):
            physics.calculate_auv2_acceleration([2, 3, 4, 5, 6], 2, 3, -3)

    def test_calculate_auv2_angular_acceleration(self):
        self.assertAlmostEqual(
            physics.calculate_auv2_angular_acceleration([1, 3, 1, 3], np.pi / 4, 3, 2),
            -0.14142135623,
        )

        self.assertNotAlmostEqual(
            physics.calculate_auv2_angular_acceleration([4, 3, 1, 5], np.pi / 6, 1, 2),
            np.sqrt(2) - np.sqrt(3) * 3,
        )

        with self.assertRaises(ValueError):
            physics.calculate_auv2_angular_acceleration(
                [3, 34, 34, 4, 3], 3, -3, -2, -5
            )

    def test_calculate

if __name__ == "__main__":
    unittest.main()
