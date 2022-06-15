#Ask the user "how many items" he wants and ask for the number of his "chosen items". (Example: "1" should be entered for the red shirt.)
 # Print the result as in the example. Example Output:
  #  Received: 2 pieces of Shirt, 2 pieces of Pants, 3 pieces of Blue, 1 piece of Red
   # Total: 4 pieces, 50.5O TL
   #Data (Items):
  
clothes = {
      #:('Type', 'Color', 'Price'),
      1:("Shirt", "Red", 10.00),
      2:("Shirt", "Blue", 11.50),
      3:("Shirt", "Yellow", 12.00),
      4:("Pants", "Red", 13.50),
      5:("Pants", "Blue", 14.00),
      6:("Pants", "Yellow", 15.50),
      7:("Tie", "Red", 16.00),
      8:("Tie", "Blue", 17.50),
      9:("Tie", "Yellow", 18.00)
}
for i in clothes: print('input [', i, '] for', clothes[i])
count = int(input('How many do you want to buy? [0-9]: '))
totals = 0
pieces = {}
for i in range(count):
  num = int(input(f'Chosing {i+1}/{count}: '))
  if (clothes[num][0] in pieces):
    pieces[clothes[num][0]] += 1
  else:
    pieces[clothes[num][0]] = 1
  if (clothes[num][1] in pieces):
    pieces[clothes[num][1]] += 1
  else:
    pieces[clothes[num][1]] = 1
  totals += clothes[num][2]
print_pieces = [(str(val) + ' pieces ' + key) for key, val in pieces.items()]
print('Purchased:', ', '.join(print_pieces))
print('Total:', count, 'Pieces =', totals, 'USD')




