from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    persons = [
        'Ридли Скотт', 'Энди Уир', 'Марк Уотни',
        'Венката Капур', 'Тедди Сандерс', 'Шон Бин'
    ]
    return render_template('distribution.html', persons=persons)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    age = 'old' if age >= 21 else 'young'
    return render_template('table.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
