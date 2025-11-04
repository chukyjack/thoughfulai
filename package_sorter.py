"""
Package Sorter for Thoughtful AI Robotic Automation Factory

This module provides functionality to sort packages based on their dimensions
and mass into appropriate stacks for automated handling.
"""


def sort(width, height, length, mass):
    """
    Sort packages into appropriate stacks based on volume and mass.
    
    A package is classified as:
    - BULKY: if volume >= 1,000,000 cm³ OR any dimension >= 150 cm
    - HEAVY: if mass >= 20 kg
    
    Packages are dispatched to:
    - STANDARD: not bulky and not heavy
    - SPECIAL: either bulky or heavy (but not both)
    - REJECTED: both bulky and heavy
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
    
    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    
    Raises:
        ValueError: If any dimension or mass is negative
        TypeError: If any parameter is not a number
    
    Examples:
        >>> sort(100, 100, 100, 10)
        'STANDARD'
        >>> sort(150, 50, 50, 10)
        'SPECIAL'
        >>> sort(100, 100, 100, 20)
        'SPECIAL'
        >>> sort(150, 50, 50, 20)
        'REJECTED'
    """
    # Input validation
    try:
        width = float(width)
        height = float(height)
        length = float(length)
        mass = float(mass)
    except (TypeError, ValueError) as e:
        raise TypeError("All parameters must be numeric values") from e
    
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")
    
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = (volume >= 1_000_000) or (width >= 150 or height >= 150 or length >= 150)
    
    # Determine if package is heavy
    is_heavy = mass >= 20
    
    # Dispatch logic
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

