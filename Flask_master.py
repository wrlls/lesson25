from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    main_data = {
        "Город": "Новочебоксарск",
        "Район": "Я держу",
        "Компания": "inet"
    }

    content = {
        'name': 'Eugene',
        'age': '26',
        'spes': 'dev'

    }
    return render_template('index.html', main_data=main_data, **content)

@app.route("/contacts/")
def contacts():
    developer_name = 'Eugene_Ustus'
    developer_phone = "978307543"


    return render_template('contacts.html', name = developer_name)

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/results/')
def results():
    data = ["cs2", "the witcher", "lada ystus", "hepl", "plsen"]
    render_template('results.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

