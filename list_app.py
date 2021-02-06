
def average(list):
  if len(list) == 0:
      return "No average for empty list"
  sum = 0
  for i in list:
    sum = sum + i
  avg = sum/len(list)
  return avg

# print(average([1, 2, 3]))

    