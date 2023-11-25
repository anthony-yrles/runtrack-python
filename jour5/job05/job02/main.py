def draw_rectangle(width, height):
  full_width = ('|' + ('-' * (width - 2)) + '|')
  empty_width = ('|' + (' ' * (width - 2)) + '|')
  rectangle = ""
  for i in range(height):
    if i == 0 or i == height - 1:
      rectangle = full_width
    else:
      rectangle = empty_width
    print(rectangle)

draw_rectangle(10, 5)