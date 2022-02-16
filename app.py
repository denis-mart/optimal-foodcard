from flask import Flask, render_template, request
from optimal_foodcard import subset_sums

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # get the data from the html form
        str_product_price = request.form['product_price_list']
        # convert the string to a list/s
        lst_product_price = [x.split(' ') for x in str_product_price.splitlines()]
        lst_product = [x[0] for x in lst_product_price]
        lst_prices = [float(x[1]) for x in lst_product_price]

        # find optimal solution
        optimal_purchase = subset_sums(lst_product, lst_prices)

        return render_template('index.html',
                                remember_input_text=str_product_price,
                                optimal_purchase1=f"1st Optimal purchase: {optimal_purchase[0]}",
                                optimal_purchase2=f"2nd Optimal purchase: {optimal_purchase[1]}",
                                optimal_purchase3=f"3rd Optimal purchase: {optimal_purchase[2]}"
                                )
    else:
        return render_template('index.html')





if __name__=="__main__":
    app.run(debug=True)