from flask import Flask, render_template

app = Flask('TimShop')

@app.route('/')
def start():
	return render_template('Новый Текстовый магазин.html')

if __name__ == '__main__':
	app.run(debug=True)
