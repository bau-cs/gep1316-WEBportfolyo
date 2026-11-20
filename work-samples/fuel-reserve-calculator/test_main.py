"""Ucus yakiti hesaplayicisi icin otomatik testler."""

import unittest

from main import calculate_fuel


class FuelCalculatorTests(unittest.TestCase):
    def test_standard_calculation(self):
        result = calculate_fuel(100.0, 30.0, 60, 30)
        self.assertAlmostEqual(result["flight_fuel_l"], 30.0)
        self.assertAlmostEqual(result["reserve_fuel_l"], 15.0)
        self.assertAlmostEqual(result["remaining_fuel_l"], 70.0)
        self.assertTrue(result["reserve_sufficient"])

    def test_reserve_is_not_sufficient(self):
        result = calculate_fuel(20.0, 60.0, 30, 30)
        self.assertAlmostEqual(result["remaining_fuel_l"], -10.0)
        self.assertFalse(result["reserve_sufficient"])

    def test_zero_reserve(self):
        result = calculate_fuel(80.0, 40.0, 60, 0)
        self.assertEqual(result["reserve_fuel_l"], 0.0)
        self.assertTrue(result["reserve_sufficient"])

    def test_negative_flight_time_rejected(self):
        with self.assertRaises(ValueError):
            calculate_fuel(80.0, 40.0, -1, 20)

    def test_zero_consumption_rejected(self):
        with self.assertRaises(ValueError):
            calculate_fuel(80.0, 0.0, 60, 20)


if __name__ == "__main__":
    unittest.main()
