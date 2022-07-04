from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def display_quote():
    if request.method == "POST":
        # getting input text in HTML form
        text = request.form['index']
        tf_text = request.form['options']
        # print(text)
        # print(tf_text)
        if text== "nasdaq" and tf_text=="option3":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nasdaq Final.csv')
            return render_template('index.html', tables=[data.iloc[[2,25,44],:].to_html()], titles=[''])
        elif text == "nasdaq" and tf_text=="option1":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/S&P500 Final.csv')
            return render_template('index.html', tables=[data.head(30).to_html()], titles=[''])
        elif text == "nasdaq" and tf_text=="option2":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/S&P500 Final.csv')
            return render_template('index.html', tables=[data.iloc[[1,6,11,16,21,26,35,40,45],:].to_html()], titles=[''])
        elif text == "s&p" and tf_text=="option3":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/S&P500 Final.csv')
            return render_template('index.html', tables=[data.iloc[[2,25,44],:].to_html()], titles=[''])
        elif text == "s&p" and tf_text=="option1":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/S&P500 Final.csv')
            return render_template('index.html', tables=[data.head(30).to_html()], titles=[''])
        elif text == "s&p" and tf_text=="option2":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/S&P500 Final.csv')
            return render_template('index.html', tables=[data.iloc[[1,6,11,16,21,26,35,40,45],:].to_html()], titles=[''])
        elif text == "dow" and tf_text=="option3":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Dow-Jones-final.csv')
            return render_template('index.html', tables=[data.iloc[[2,25,44],:].to_html()], titles=[''])
        elif text == "dow" and tf_text=="option1":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Dow-Jones-final.csv')
            return render_template('index.html', tables=[data.head(30).to_html()], titles=[''])
        elif text == "dow" and tf_text=="option2":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Dow-Jones-final.csv')
            return render_template('index.html', tables=[data.iloc[[1,6,11,16,21,26,35,40,45],:].to_html()], titles=[''])
        elif text == "nifty" and tf_text=="option1" :
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Final.csv')
            return render_template('index.html', tables=[data.head(30).to_html()], titles=[''])
        elif text == "nifty" and tf_text=="option2":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Final.csv')
            return render_template('index.html', tables=[data.iloc[[1,6,11,16,21,26,31,36,41,46],:].to_html()], titles=[''])
        elif text == "nifty" and tf_text=="option3":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Final.csv')
            return render_template('index.html', tables=[data.iloc[[2,23,41],:].to_html()], titles=[''])
        elif text == "bank nifty" and tf_text=="option1":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Bank Final.csv')
            return render_template('index.html', tables=[data.head(30).to_html()], titles=[''])
        elif text == "bank nifty" and tf_text=="option2":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Bank Final.csv')
            return render_template('index.html', tables=[data.iloc[[1,6,11,16,21,26,31,36,41,46],:].to_html()], titles=[''])
        elif text == "bank nifty" and tf_text=="option3":
            data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nifty Bank Final.csv')
            return render_template('index.html', tables=[data.iloc[[2,23,41],:].to_html()], titles=[''])

    return render_template("index.html")
if __name__ == '__main__':
	app.run()


# # importing flask
# from flask import Flask, render_template

# # importing pandas module
# import pandas as pd


# app = Flask(__name__)


# # reading the data in the csv file
# df = pd.read_csv('C:/Users/AKUMA982/Downloads/Nasdaq Final.csv')
# df.to_csv('C:/Users/AKUMA982/Downloads/Nasdaq Final.csv', index=None)


# # route to html page - "table"
# @app.route('/')
# @app.route('/table')
# def table():
	
# 	# converting csv to html
# 	data = pd.read_csv('C:/Users/AKUMA982/Downloads/Nasdaq Final.csv')
# 	return render_template('index.html', tables=[data.to_html()], titles=[''])


# if __name__ == "__main__":
# 	app.run()

