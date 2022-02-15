from flask import Flask, render_template, request
from optimal_foodcard import subset_sums

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # get the data from the html table
        list_prods = [request.form[f'prod0{i}'] for i in range(1,5)]
        list_prices = [float(request.form[f'price0{i}']) for i in range(1,5)]

        # find optimal solution
        optimal_purchase = subset_sums(list_prods, list_prices)

        return render_template('index.html',
                                optimal_purchase1=f"1st Optimal purchase: {optimal_purchase[0]}",
                                optimal_purchase2=f"2nd Optimal purchase: {optimal_purchase[1]}",
                                optimal_purchase3=f"3rd Optimal purchase: {optimal_purchase[2]}"
                                )
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)