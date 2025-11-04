"""
Unit tests for the package sorter module.

Tests cover all classification scenarios, edge cases, and error handling.
"""

import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """Test cases for the package sorting function."""
    
    # STANDARD packages (not bulky, not heavy)
    def test_standard_small_package(self):
        """Test small package with low mass."""
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
    
    def test_standard_medium_package(self):
        """Test medium-sized package just under bulky threshold."""
        self.assertEqual(sort(100, 100, 99, 10), "STANDARD")
    
    def test_standard_at_dimension_boundary(self):
        """Test package with dimensions just below 150 cm threshold."""
        # Note: 149x149x149 = 3,307,949 cm³ which is > 1,000,000, so it's SPECIAL
        self.assertEqual(sort(149, 50, 50, 19), "STANDARD")
    
    def test_standard_at_mass_boundary(self):
        """Test package with mass just below 20 kg threshold."""
        self.assertEqual(sort(50, 50, 50, 19.99), "STANDARD")
    
    # SPECIAL packages (bulky OR heavy, but not both)
    def test_special_bulky_by_volume(self):
        """Test package that is bulky due to volume >= 1,000,000 cm³."""
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # volume = 1,000,000
    
    def test_special_bulky_by_width(self):
        """Test package that is bulky due to width >= 150 cm."""
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
    
    def test_special_bulky_by_height(self):
        """Test package that is bulky due to height >= 150 cm."""
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
    
    def test_special_bulky_by_length(self):
        """Test package that is bulky due to length >= 150 cm."""
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
    
    def test_special_bulky_by_multiple_dimensions(self):
        """Test package with multiple dimensions at or above threshold."""
        self.assertEqual(sort(150, 150, 50, 5), "SPECIAL")
    
    def test_special_heavy_only(self):
        """Test package that is heavy but not bulky."""
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
    
    def test_special_very_heavy(self):
        """Test very heavy package that is not bulky."""
        self.assertEqual(sort(10, 10, 10, 100), "SPECIAL")
    
    def test_special_just_over_volume_threshold(self):
        """Test package just over the volume threshold."""
        self.assertEqual(sort(100, 100, 100.01, 19), "SPECIAL")
    
    # REJECTED packages (both bulky AND heavy)
    def test_rejected_bulky_and_heavy(self):
        """Test package that is both bulky (by dimension) and heavy."""
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
    
    def test_rejected_bulky_by_volume_and_heavy(self):
        """Test package that is both bulky (by volume) and heavy."""
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
    
    def test_rejected_all_dimensions_large_and_heavy(self):
        """Test very large and heavy package."""
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
    
    def test_rejected_at_both_boundaries(self):
        """Test package at exactly both thresholds."""
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")
    
    # Edge cases
    def test_zero_dimensions_and_mass(self):
        """Test package with all zero values."""
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
    
    def test_zero_mass_bulky_dimensions(self):
        """Test bulky package with zero mass."""
        self.assertEqual(sort(150, 50, 50, 0), "SPECIAL")
    
    def test_zero_dimensions_heavy_mass(self):
        """Test heavy package with zero dimensions."""
        self.assertEqual(sort(0, 0, 0, 20), "SPECIAL")
    
    def test_very_large_values(self):
        """Test with very large dimension and mass values."""
        self.assertEqual(sort(10000, 10000, 10000, 1000), "REJECTED")
    
    def test_decimal_values(self):
        """Test with decimal dimension and mass values."""
        # 149.9x149.9x149.9 = 3,367,299.899 cm³ which is > 1,000,000, so it's SPECIAL
        self.assertEqual(sort(50, 50, 50, 19.9), "STANDARD")  # Just below mass threshold
        self.assertEqual(sort(150.1, 50, 50, 20.1), "REJECTED")  # Both bulky and heavy
    
    # Input validation tests
    def test_negative_dimension_raises_error(self):
        """Test that negative dimensions raise ValueError."""
        with self.assertRaises(ValueError):
            sort(-10, 50, 50, 10)
    
    def test_negative_mass_raises_error(self):
        """Test that negative mass raises ValueError."""
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -5)
    
    def test_string_input_raises_error(self):
        """Test that non-numeric string input raises TypeError."""
        with self.assertRaises(TypeError):
            sort("abc", 50, 50, 10)
    
    def test_none_input_raises_error(self):
        """Test that None input raises TypeError."""
        with self.assertRaises(TypeError):
            sort(None, 50, 50, 10)
    
    def test_numeric_string_is_converted(self):
        """Test that numeric strings are properly converted."""
        self.assertEqual(sort("100", "100", "100", "10"), "SPECIAL")
    
    # Boundary value tests
    def test_exact_volume_boundary(self):
        """Test package at exactly 1,000,000 cm³."""
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    
    def test_just_below_volume_boundary(self):
        """Test package just below 1,000,000 cm³."""
        self.assertEqual(sort(100, 100, 99.99, 10), "STANDARD")
    
    def test_exact_dimension_boundary(self):
        """Test package at exactly 150 cm dimension."""
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
    
    def test_just_below_dimension_boundary(self):
        """Test package just below 150 cm dimension."""
        self.assertEqual(sort(149.99, 50, 50, 10), "STANDARD")
    
    def test_exact_mass_boundary(self):
        """Test package at exactly 20 kg."""
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
    
    def test_just_below_mass_boundary(self):
        """Test package just below 20 kg."""
        self.assertEqual(sort(50, 50, 50, 19.99), "STANDARD")


def run_tests():
    """Run all tests and return results."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestPackageSorter))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)

