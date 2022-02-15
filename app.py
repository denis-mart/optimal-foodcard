from flask import Flask, render_template, request
#from optimal_foodcard import subset_sums

app = Flask(__name__)

# function to find subset of prices that would be closer to food card asignment
def subset_sums(prods, prices, target=10, number_optimals=3):
   '''
   Finds the subset of prices that would be closer to the target amount
   '''
   lst_posible_sets = []
   lst_sum = []
   n = len(prices)
   # There are total 2^n subsets
   total = 1 << n

   # Consider all numbers from 0 to 2^n - 1
   for i in range(total):
      sum = 0

      # Consider binary representation of
      # current i to decide which elements
      # to pick.
      lst_prices = []
      for j in range(n):
         if ((i & (1 << j)) != 0):
            lst_prices.append(j)
            sum += prices[j]

      if sum >= target:
         lst_posible_sets.append(lst_prices)
         lst_sum.append(sum)
   
   # position(s) of the minimum(s) (above target) of lst_sum
   min_sum = sorted(lst_sum)[:number_optimals]
   min_pos = [lst_sum.index(i) for i in min_sum]
   best_choice = [lst_posible_sets[i] for i in min_pos]
   products_best_choice = [[prods[i] for i in j] for j in best_choice]
   prices_best_choice = [[prices[i] for i in j] for j in best_choice]
   min_sum_rounded = list(map(lambda x: round(x,2) , min_sum ))

   #return best_choice, products_best_choice, prices_best_choice, min_sum_rounded
   
   # zip every element in the list of lists into a list of tuples
   list_of_optimal_products_prices = [ list(zip(x, y)) for x, y in zip(products_best_choice, prices_best_choice)]
   
   return list(zip(min_sum_rounded, list_of_optimal_products_prices))


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