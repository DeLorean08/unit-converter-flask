from flask import Flask, render_template, request
from logic import LengthConverter, WeightConverter, TemperatureConverter

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def length():
    result = None
    error = None
    if request.method == "POST":
        val_str = request.form.get('val_to_convert')
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        try:
            value = float(val_str)
            result = LengthConverter.convert(value, unit_from, unit_to)
        except ValueError as e:
            error = str(e)
    return render_template('length.html', result=result, error=error)

@app.route("/weight", methods=['GET', 'POST'])
def weight():
    result = None
    error = None
    if request.method == "POST":
        val_str = request.form.get('val_to_convert')
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        try:
            value = float(val_str)
            result = WeightConverter.convert(value, unit_from, unit_to)
        except ValueError as e:
            error = str(e)
    return render_template('weight.html', result=result, error=error)

@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    result = None
    error = None
    if request.method == "POST":
        val_str = request.form.get('val_to_convert')
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')
        try:
            value = float(val_str)
            result = TemperatureConverter.convert(value, unit_from, unit_to)
        except ValueError as e:
            error = str(e)
    return render_template('temp.html', result=result, error=error)

        

if __name__ == '__main__':
    app.run(debug=True)