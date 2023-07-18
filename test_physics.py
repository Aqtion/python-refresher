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

    def test_simulate_auv2_motion(self):
        tup = physics.simulate_auv2_motion(
            [40, 80, 120, 160], np.pi / 3, 3, 2, 100, 100, 0.1, 0.4
        )

        self.assertTrue(
            np.allclose(
                np.array(tup[0]),
                [0.0, 0.1, 0.2, 0.3],
            )
        )
        self.assertTrue(
            np.allclose(
                np.array(tup[1]),
                [0.0, 0.0, -0.008, -0.024],
            )
        )
        self.assertTrue(np.allclose(np.array(tup[2]), [0.0, 0.0, 0.0, 0.0]))
        self.assertTrue(
            np.allclose(np.array(tup[3]), [0.0, 0.0, -0.02878461, -0.08635383])
        )
        self.assertTrue(
            np.allclose(
                np.array(tup[4]),
                [
                    [0.0, 0.0],
                    [-0.08000000000000003, 0.0],
                    [-0.16000000000000006, 0.0],
                    [-0.2400000000000001, 0.0],
                ],
            ),
        )
        self.assertTrue(
            np.allclose(np.array(tup[5]), [0.0, -0.2878461, -0.57569219, -0.86353829])
        )
        self.assertTrue(
            np.allclose(
                np.array(tup[6]),
                [
                    [-0.8000000000000003, 0.0],
                    [-0.8000000000000003, 0.0],
                    [-0.8000000000000003, 0.0],
                    [-0.7996686013807245, 0.023024507938203508],
                ],
            )
        )

        (
            t_test,
            x_test,
            y_test,
            theta_test,
            v_test,
            omega_test,
            a_test,
        ) = physics.simulate_auv2_motion(
            np.array([1, 0, 1, 0]), 0.5, 1.5, 1.8, dt=0.5, t_final=1.5
        )
        self.assertEqual(t_test[0], 0)
        self.assertEqual(t_test[1], 0.5)
        self.assertEqual(t_test[2], 1.0)
        self.assertEqual(np.all(x_test), 0)
        self.assertEqual(np.all(y_test), 0)
        self.assertEqual(theta_test[0], 0)
        self.assertEqual(theta_test[1], 0)
        self.assertEqual(theta_test[2], 0.011493934596544877)
        self.assertEqual(np.all(v_test), 0)
        self.assertEqual(np.all(a_test), 0)
        self.assertEqual(omega_test[0], 0)
        self.assertEqual(omega_test[1], 0.022987869193089754, 0.04597574)

        with self.assertRaises(ValueError):
            physics.simulate_auv2_motion([3, 4, 5, 6, 5], 3, -3, -3)


if __name__ == "__main__":
    unittest.main()
