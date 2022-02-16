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
   min_sum_rounded = [round(i,2) for i in min_sum]

   #return best_choice, products_best_choice, prices_best_choice, min_sum_rounded
   
   # zip every element in the list of lists into a list of tuples
   list_of_optimal_products_prices = [ list(zip(x, y)) for x, y in zip(products_best_choice, prices_best_choice)]
   
   return list(zip(min_sum_rounded, list_of_optimal_products_prices))

   
