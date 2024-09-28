from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
  name = request.form['name']
  age = request.form['age']
  address = request.form['address']
  city = request.form['city']
  state = request.form['state']
  zip_code = request.form['zip_code']
  profession = request.form['profession']
  hobbies = request.form.getlist('hobbies')
  about_me = request.form['about_me']
  #Return personalized message to the user
  return render_template('submit.html', name=name, age=age, address=address, city=city, state=state, zip_code=zip_code, profession=profession, hobbies=hobbies, about_me=about_me)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')