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
git clone https://github.com/chukyjack/thoughfulai.git
cd thoughfulai
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


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


## Project Structure

```
thoughfulai/
│
├── package_sorter.py          # Main implementation
├── test_package_sorter.py     # Comprehensive test suite
├── README.md                   # This file
└── requirements.txt            # Python dependencies (none required)
```

## Author

Created by Chuka for Thoughtful AI Technical Challenge

## License

This project is created for evaluation purposes.

