def unique_elements(list):
  unique_list = []
  for item in list:
    if item not in unique_list:
      unique_list.append(item)
  print(unique_list)

unique_elements([1, 2, 2, 3, 4, 4, 5])