from flask import Flask, render_template, request, jsonify
import urllib.request
import pandas as pd
from pandas import ExcelWriter


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'DontTellAnyone'


@app.route('/get_stocks', methods=['POST'])
def get_stocks():

	stocks_list = []
	for i in range(1, 11):
		if request.form['company' + str(i)] != '':
			stocks_list.append(request.form['company' + str(i)])


	print(stocks_list)
	stocks_json = {}
	for item in stocks_list:
		print(item)
		earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings?day=2019-06-13&symbol=' + str(item))[0]
		latest_earnings = earnings['Earnings Date'].tolist()[:4]
		stocks_json[item] = latest_earnings
		
	return render_template('show_earnings.html', stocks_json=stocks_json)



"""
@app.route('/get_stocks/<string:stocks_list>', methods=['GET'])
def get_stocks(stocks_list):
	stocks_list = stocks_list.split(',')
	print(stocks_list)
	stocks_json = {}
	for item in stocks_list:
		print(item)
		earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings?day=2019-06-13&symbol=' + str(item))[0]
		latest_earnings = earnings['Earnings Date'].tolist()[:4]
		stocks_json[item] = latest_earnings
	return jsonify(stocks_json)
"""

@app.route('/', methods=['GET', 'POST'])
def index():
	#form = LoginForm()
	return render_template('index.html') #, form=form)



# list = ['TextField']
#xls_path = '/Users/tony/documents/Python_Projects/test_prices_2.xlsx'

#writer = pd.ExcelWriter(xls_path, engine='xlsxwriter')

# for item in list:
#     print (item)

# for item in list:
#     earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings?day=2019-06-13&symbol=' + str(item))[0]
#     latest_earnings = earnings[:4]
#     print (latest_earnings)
#   print ('\n This is the price for:' + str(item) + '\n')    
#   prices = pdr.get_data_yahoo(item)[-30:]
#   print (prices)
    
#   prices.to_excel(writer, item)

#writer.save()



if __name__ == '__main__':
	app.run(debug=True)