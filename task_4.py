new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))#Перенеси её из списка new_tasks в список completed_tasks. Сделай это в одно действие.

print('задание  1')
print('new_tasks',new_tasks)
print('completed_tasks',completed_tasks)

new_tasks.pop(new_tasks.index('task_007')) #Удали его из списка new_tasks.

print('задание  2')
print('new_tasks',new_tasks)
print('completed_tasks',completed_tasks)

print('задание  3')
print(new_tasks[-1]) #В последней задаче из списка new_tasks заказчик поднял приоритет, поэтому её нужно будет взять в работу следующей.


print('new_tasks',new_tasks)
print('completed_tasks',completed_tasks)