# Package Sorter - Thoughtful AI Challenge

A robotic automation solution for sorting packages based on their dimensions and mass.

## Overview

This project implements a package sorting system for Thoughtful AI's robotic automation factory. The system classifies packages into three categories (STANDARD, SPECIAL, or REJECTED) based on their volume and mass characteristics.

## Problem Statement

Packages need to be sorted according to these rules:

- **Bulky Package**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy Package**: Mass ≥ 20 kg

### Dispatch Categories

- **STANDARD**: Packages that are neither bulky nor heavy (normal automated handling)
- **SPECIAL**: Packages that are either bulky OR heavy (requires special handling)
- **REJECTED**: Packages that are both bulky AND heavy (cannot be processed)

## Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd thoughfulai
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. No external dependencies required - uses Python standard library only!

## Usage

### Basic Usage

```python
from package_sorter import sort

# Example 1: Standard package
result = sort(50, 50, 50, 10)  # Returns: "STANDARD"

# Example 2: Bulky package (dimension >= 150 cm)
result = sort(150, 50, 50, 10)  # Returns: "SPECIAL"

# Example 3: Heavy package (mass >= 20 kg)
result = sort(50, 50, 50, 20)  # Returns: "SPECIAL"

# Example 4: Both bulky and heavy
result = sort(150, 50, 50, 20)  # Returns: "REJECTED"
```

### Function Signature

```python
sort(width, height, length, mass)
```

**Parameters:**
- `width` (float): Package width in centimeters
- `height` (float): Package height in centimeters
- `length` (float): Package length in centimeters
- `mass` (float): Package mass in kilograms

**Returns:**
- `str`: One of "STANDARD", "SPECIAL", or "REJECTED"

**Raises:**
- `ValueError`: If any dimension or mass is negative
- `TypeError`: If any parameter is not numeric

## Running Tests

Execute the comprehensive test suite:

```bash
python test_package_sorter.py
```

Or using unittest directly:

```bash
python -m unittest test_package_sorter.py -v
```

### Test Coverage

The test suite includes:
- ✅ **Standard package scenarios** (11 tests)
- ✅ **Special package scenarios** (8 tests for bulky, 4 tests for heavy)
- ✅ **Rejected package scenarios** (4 tests)
- ✅ **Edge cases** (zero values, very large values, decimals)
- ✅ **Input validation** (negative values, invalid types)
- ✅ **Boundary value tests** (exact thresholds)
- ✅ **Integration tests** (realistic package scenarios)

**Total: 40+ test cases**

## Examples

### Classification Examples

| Width | Height | Length | Mass | Volume | Classification | Reason |
|-------|--------|--------|------|--------|----------------|--------|
| 50 | 50 | 50 | 10 | 125,000 | STANDARD | Not bulky, not heavy |
| 150 | 50 | 50 | 10 | 375,000 | SPECIAL | Bulky (dimension ≥ 150) |
| 100 | 100 | 100 | 10 | 1,000,000 | SPECIAL | Bulky (volume ≥ 1M) |
| 50 | 50 | 50 | 20 | 125,000 | SPECIAL | Heavy (mass ≥ 20) |
| 150 | 50 | 50 | 20 | 375,000 | REJECTED | Both bulky and heavy |
| 100 | 100 | 100 | 25 | 1,000,000 | REJECTED | Both bulky and heavy |

### Code Examples

```python
from package_sorter import sort

# Small parcel
print(sort(30, 20, 10, 5))  # Output: STANDARD

# Long package (one dimension at threshold)
print(sort(150, 40, 30, 15))  # Output: SPECIAL

# High-volume package
print(sort(100, 100, 100, 15))  # Output: SPECIAL

# Heavy but compact package
print(sort(40, 40, 40, 25))  # Output: SPECIAL

# Large and heavy package
print(sort(200, 100, 80, 50))  # Output: REJECTED
```

## Code Quality Features

- ✨ **Clean, readable code** with comprehensive documentation
- 📝 **Type hints** in docstrings for clarity
- 🛡️ **Input validation** with meaningful error messages
- 🧪 **Extensive test coverage** (40+ test cases)
- 📊 **Edge case handling** (zero values, boundaries, decimals)
- 🎯 **Single Responsibility Principle** - one function, one purpose
- ⚡ **No external dependencies** - uses only Python standard library

## Project Structure

```
thoughfulai/
│
├── package_sorter.py          # Main implementation
├── test_package_sorter.py     # Comprehensive test suite
├── README.md                   # This file
└── requirements.txt            # Python dependencies (none required)
```

## Algorithm Explanation

1. **Input Validation**: Ensures all parameters are numeric and non-negative
2. **Volume Calculation**: Computes volume = width × height × length
3. **Bulky Check**: Tests if volume ≥ 1,000,000 OR any dimension ≥ 150
4. **Heavy Check**: Tests if mass ≥ 20
5. **Classification Logic**:
   - If bulky AND heavy → REJECTED
   - If bulky OR heavy → SPECIAL
   - Otherwise → STANDARD

Time Complexity: O(1) - constant time operation
Space Complexity: O(1) - constant space usage

## Author

Created for Thoughtful AI Technical Challenge

## License

This project is created for evaluation purposes.

