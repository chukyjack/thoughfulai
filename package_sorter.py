"""
Package Sorter for Thoughtful AI Robotic Automation Factory

This module provides functionality to sort packages based on their dimensions
and mass into appropriate stacks for automated handling.

Public API:
    sort(width, height, length, mass) -> str

Private helpers:
    _validate_and_convert_inputs() - Input validation and type conversion
    _is_bulky() - Check if package is bulky
    _is_heavy() - Check if package is heavy
"""


def _validate_and_convert_inputs(width, height, length, mass):
    """
    Validate and convert package parameters to floats.
    
    Args:
        width: Package width (numeric or convertible to float)
        height: Package height (numeric or convertible to float)
        length: Package length (numeric or convertible to float)
        mass: Package mass (numeric or convertible to float)
    
    Returns:
        tuple: (width, height, length, mass) as floats
    
    Raises:
        TypeError: If any parameter cannot be converted to a number
        ValueError: If any parameter is negative
    """
    # Convert to float
    try:
        width = float(width)
        height = float(height)
        length = float(length)
        mass = float(mass)
    except (TypeError, ValueError) as e:
        raise TypeError("All parameters must be numeric values") from e
    
    # Validate non-negative
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")
    
    return width, height, length, mass


def _is_bulky(width, height, length):
    """
    Determine if a package is bulky.
    
    A package is bulky if:
    - Volume >= 1,000,000 cm³, OR
    - Any dimension >= 150 cm
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
    
    Returns:
        bool: True if package is bulky, False otherwise
    """
    volume = width * height * length
    return volume >= 1_000_000 or max(width, height, length) >= 150


def _is_heavy(mass):
    """
    Determine if a package is heavy.
    
    A package is heavy if mass >= 20 kg.
    
    Args:
        mass (float): Package mass in kilograms
    
    Returns:
        bool: True if package is heavy, False otherwise
    """
    return mass >= 20


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
    # Validate and convert inputs
    width, height, length, mass = _validate_and_convert_inputs(width, height, length, mass)
    
    # Determine package characteristics
    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)
    
    # Dispatch logic
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

