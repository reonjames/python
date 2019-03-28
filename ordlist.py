def sort_list_last(xo):
  xo.sort(key=lambda x: x[1])
  print(xo)

sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])