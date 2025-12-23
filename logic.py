class LengthConverter:
    factors = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0, 
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }

    @staticmethod
    def convert(value: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()
        
        if value < 0:
            raise ValueError("Length cannot be less than zero")
            
        if unit_from == unit_to:
            return value
            
        if unit_from in LengthConverter.factors and unit_to in LengthConverter.factors:
            result = LengthConverter.factors[unit_from] * value / LengthConverter.factors[unit_to]
            return round(result, 4)
            
        raise ValueError("Invalid unit of measurement")

    
class TemperatureConverter:
    factors = {
        ('celsius', 'fahrenheit'): lambda val: (val * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda val: (val - 32) * 5/9,
        ('celsius', 'kelvin'): lambda val: val + 273.15,
        ('kelvin', 'celsius'): lambda val: val - 273.15,
        ('fahrenheit', 'kelvin'): lambda val: (val - 32) * 5/9 + 273.15,
        ('kelvin', 'fahrenheit'): lambda val: (val - 273.15) * 9/5 + 32
    }

    limits = {
        'celsius': -273.15,
        'fahrenheit': -459.67,
        'kelvin': 0
    }

    @staticmethod
    def convert(value: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()
        
        if unit_from in TemperatureConverter.limits:
            if value < TemperatureConverter.limits[unit_from]:
                limit_val = TemperatureConverter.limits[unit_from]
                raise ValueError(f"Temperature is below absolute zero ({limit_val} {unit_from})")
                
        if unit_from == unit_to:
            return value
            
        if (unit_from, unit_to) in TemperatureConverter.factors:
            result = TemperatureConverter.factors[(unit_from, unit_to)](value)
            return round(result, 4)
            
        raise ValueError(f"Conversion from {unit_from} to {unit_to} is not supported")


class WeightConverter:
    factors = {
        "milligram": 0.001,
        "gram": 1.0,
        "kilogram": 1000.0,
        "ounce": 28.3495, 
        "pound": 453.592,
    }

    @staticmethod
    def convert(value: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()
        
        if value < 0:
            raise ValueError("Weight cannot be less than zero")
            
        if unit_from == unit_to:
            return value
            
        if unit_from in WeightConverter.factors and unit_to in WeightConverter.factors:
            result = WeightConverter.factors[unit_from] * value / WeightConverter.factors[unit_to]
            return round(result, 4)
            
        raise ValueError("Invalid unit of measurement")