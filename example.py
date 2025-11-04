#!/usr/bin/env python3
"""
Example usage of the package sorter function.

This script demonstrates various package classifications.
"""

from package_sorter import sort


def print_classification(width, height, length, mass, description=""):
    """Print the classification result for a package."""
    result = sort(width, height, length, mass)
    volume = width * height * length
    
    print(f"\n{description}")
    print(f"  Dimensions: {width} x {height} x {length} cm")
    print(f"  Volume: {volume:,.0f} cm³")
    print(f"  Mass: {mass} kg")
    print(f"  Classification: {result}")


def main():
    """Run example classifications."""
    print("=" * 60)
    print("PACKAGE SORTER - EXAMPLE CLASSIFICATIONS")
    print("=" * 60)
    
    # STANDARD packages
    print("\n--- STANDARD PACKAGES ---")
    print_classification(30, 20, 10, 5, "Small parcel (book)")
    print_classification(50, 40, 30, 15, "Medium box (electronics)")
    print_classification(80, 60, 50, 18, "Large box (clothing)")
    
    # SPECIAL packages (bulky)
    print("\n--- SPECIAL PACKAGES (Bulky) ---")
    print_classification(150, 50, 40, 10, "Long package (skiing equipment)")
    print_classification(100, 100, 100, 15, "High-volume cube")
    print_classification(200, 80, 60, 18, "Furniture piece")
    
    # SPECIAL packages (heavy)
    print("\n--- SPECIAL PACKAGES (Heavy) ---")
    print_classification(40, 40, 40, 25, "Compact but heavy (tools)")
    print_classification(60, 50, 40, 35, "Heavy equipment")
    
    # REJECTED packages
    print("\n--- REJECTED PACKAGES ---")
    print_classification(150, 80, 60, 25, "Large and heavy (machinery)")
    print_classification(200, 150, 100, 50, "Industrial equipment")
    
    # Edge cases
    print("\n--- EDGE CASES ---")
    print_classification(150, 50, 50, 20, "At both thresholds exactly")
    print_classification(149.99, 50, 50, 19.99, "Just below both thresholds")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

