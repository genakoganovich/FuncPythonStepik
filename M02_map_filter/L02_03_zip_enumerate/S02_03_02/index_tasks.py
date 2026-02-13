tasks = ['Помыть посуду', 'Выучить Python', 'Сделать зарядку']

# Мы сразу распаковываем кортеж (0, 'Помыть посуду') в переменные index и task
for index, task in enumerate(tasks):
  print(f"{index}: {task}")