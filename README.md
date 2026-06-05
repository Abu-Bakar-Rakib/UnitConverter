# UnitConverter

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-Active-brightgreen?style=flat-square)

A comprehensive and intuitive Python library for converting between various units of measurement across multiple categories.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## 🎯 Overview

UnitConverter is a lightweight, extensible Python library designed to simplify unit conversions across diverse domains including length, weight, temperature, volume, time, and more. Whether you're building scientific applications, educational tools, or data processing pipelines, UnitConverter provides a clean API for accurate and efficient unit transformations.

## ✨ Features

- **Multi-Category Support** - Convert across length, weight, temperature, volume, time, and more
- **High Accuracy** - Precise conversion factors based on international standards
- **Easy-to-Use API** - Intuitive methods for seamless integration
- **Extensible Architecture** - Add custom units and conversion categories with ease
- **Lightweight** - Minimal dependencies for fast installation and execution
- **Well-Documented** - Comprehensive documentation with practical examples
- **Fully Tested** - Robust test coverage ensuring reliability

## 📋 Supported Unit Categories

- **Length**: meters, kilometers, miles, yards, feet, inches, centimeters, millimeters, and more
- **Weight/Mass**: kilograms, grams, pounds, ounces, tons, and more
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Volume**: liters, milliliters, gallons, cups, pints, and more
- **Time**: seconds, minutes, hours, days, weeks, months, years
- **Area**: square meters, square kilometers, acres, square miles, and more

## 🚀 Quick Start

### Installation

```bash
pip install unitconverter
```

Or install from source:

```bash
git clone https://github.com/Abu-Bakar-Rakib/UnitConverter.git
cd UnitConverter
pip install -e .
```

### Basic Usage

```python
from unitconverter import UnitConverter

# Initialize the converter
converter = UnitConverter()

# Convert length
result = converter.convert(100, 'meters', 'kilometers')
print(f"100 meters = {result} kilometers")  # Output: 100 meters = 0.1 kilometers

# Convert temperature
celsius_to_fahrenheit = converter.convert(25, 'celsius', 'fahrenheit')
print(f"25°C = {celsius_to_fahrenheit}°F")

# Convert weight
kg_to_lbs = converter.convert(70, 'kilograms', 'pounds')
print(f"70 kg = {kg_to_lbs} lbs")
```

## 📚 Documentation

### Core Methods

#### `convert(value, from_unit, to_unit)`

Converts a value from one unit to another.

**Parameters:**
- `value` (float): The value to convert
- `from_unit` (str): The source unit
- `to_unit` (str): The target unit

**Returns:** float - The converted value

**Example:**
```python
result = converter.convert(1, 'mile', 'kilometer')
# result: 1.60934
```

### Advanced Features

#### Custom Unit Definitions

```python
converter.add_custom_unit('my_unit', 'length', 5.0)  # 1 my_unit = 5 meters
```

#### Batch Conversions

```python
values = [10, 20, 30]
results = converter.batch_convert(values, 'miles', 'kilometers')
```

## 💡 Use Cases

- **Scientific Research**: Convert measurements in physics, chemistry, and biology experiments
- **Engineering Projects**: Handle unit conversions in design and construction workflows
- **Educational Tools**: Teach students about unit conversions with practical examples
- **Data Processing**: Normalize measurement data from various sources
- **Global Applications**: Handle multiple measurement systems across regions

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines
- Tests are included for new features
- Documentation is updated accordingly

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=unitconverter
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and standard library best practices
- Conversion factors verified against international standards (SI, NIST)
- Inspired by the need for a simple, reliable unit conversion tool

## 📧 Support

For questions, issues, or suggestions:

- **GitHub Issues**: [Create an issue](https://github.com/Abu-Bakar-Rakib/UnitConverter/issues)
- **Discussions**: [Join the discussion](https://github.com/Abu-Bakar-Rakib/UnitConverter/discussions)

---

<div align="center">

Made with ❤️ by [Abu-Bakar-Rakib](https://github.com/Abu-Bakar-Rakib)

[⬆ Back to top](#unitconverter)

</div>
