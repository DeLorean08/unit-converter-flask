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
            raise ValueError("Довжина не може бути меншою за нуль")
        if unit_from == unit_to:
            return value
        if unit_from in LengthConverter.factors and unit_to in LengthConverter.factors:
            result = LengthConverter.factors[unit_from] * value / LengthConverter.factors[unit_to]
            return round(float(result), 4)
        raise ValueError("Не існуюча одиниця виміру")
           
    
class TemperatureConverter:
    factors = {
        ('celsius', 'fahrenheit'):  lambda val: (val * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda val: (val - 32) * 5/9,
        ('celsius', 'kelvin'): lambda val: val + 273.15,
        ('kelvin', 'celsius'): lambda val: val - 273.15,
        ('fahrenheit', 'kelvin'): lambda val: (val - 32) * 5/9 + 273.15,
        ('kelvin', 'fahrenheit'): lambda val: (val - 273.15)* 9/5 + 32
    }

    @staticmethod
    def convert(value: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()
        if unit_from == "kelvin" and value < 0:
            raise ValueError("Кельвін не може бути менше 0")
        if unit_from == unit_to:
            return value
        if (unit_from, unit_to) in TemperatureConverter.factors:
            result = TemperatureConverter.factors[(unit_from, unit_to)](value)
            return round(float(result), 4)
        raise ValueError(f"Конвертація з {unit_from} у {unit_to} не підтримується")

class WeightConverter:
    factors = {
        "milligram": 0.001,
        "gram": 1.0,
        "kilogram": 1000.0,
        "ounce": 28.3495, 
        "pound": 453.592,
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
        if unit_from in WeightConverter.limits:
            if value < WeightConverter.limits[unit_from]:
                limit_val = WeightConverter.limits[unit_from]
                raise ValueError(f"Температура нижче абсолютного нуля ({limit_val} {unit_from})")
        if unit_from == unit_to:
            return value
        if unit_from in WeightConverter.factors and unit_to in WeightConverter.factors:
            result = WeightConverter.factors[unit_from] * value / WeightConverter.factors[unit_to]
            return round(float(result), 4)
        raise ValueError("Не існуюча одиниця виміру")