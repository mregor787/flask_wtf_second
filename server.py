from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    persons = [
        'Ридли Скотт', 'Энди Уир', 'Марк Уотни',
        'Венката Капур', 'Тедди Сандерс', 'Шон Бин'
    ]
    return render_template('distribution.html', persons=persons)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
