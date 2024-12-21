class TodoApp:
	'''A simple  implementation of a Todo app'''
	
	tasks =[] # all task are stored here 
	def __init__(self):
		self.name=input('What\'s your name: ')
		print(f"WELCOME TO YOUR TODO APP {self.name.upper()}")
		TodoApp.ui(self)
		
	def list_tasks(self):
		'''List alltask that has been added to the TodoApp class variable (tasks = [])'''
		if  TodoApp.tasks==[]: 
			print('No task added')
		self.num = 1
		for task in TodoApp.tasks:
				print(f'Tasks {self.num}')
				print('='*20)
				print(task)
				
				self.num+=1
			
	def add_task(self):
		'''Adds the tasks to the TodoApp class variable (tasks = [])'''
		print("Add Task")
		self.new = input('Enter task=>')
		
		TodoApp.tasks.append(self.new)	
		
	def delete_task(self):
		'''Uses the .remove() method  to delete a single item  in the list'''
		print('Delete Task')
		self.task  = input('enter task=>')
		if self.task in TodoApp.tasks:
			TodoApp.tasks.remove(self.task)
			print('Task deleted sucessfully')
		else:
			print('Task not in your todo list enter 1 to list all task!!')
	def clear(self):
		'''It removes all the tasks  in the TodoAppclass variable  '(tasks=[])' '''
		print("Task Cleared")
		TodoApp.tasks.clear()
	
	def save(self):
		'''It write all the tasks  added to the TodoApp class variable '(tasks[])' into a text file '''
		self.num = 1
		self.filename= 'Todolist.txt'
		with open(self.filename, "a") as f:
		       f.write(f"Todo list\n")
		       for line in TodoApp.tasks:
		           f.write(f"{self.num} {line} ✅❌" + "\n")
		           
		           self.num+=1
		       f.write('\n')
		       print(f"Saved successfully in '{self.filename}'")
        
		
	def ui(self):
		'''It contains  the logic and User interface of the program'''
		
		while True :
			print('='*20)
			print('Enter 1 to  list tasks')
			print('Enter 2 to add tasks')
			print('Enter 3 to delete tasks')
			print('Enter 4 to save tasks')
			print('Enter c to clear list')
			print('Enter q to quit'.strip())
			print('='*20)
			self.input = input('=> ').strip()
			if self.input =='1':
				TodoApp.list_tasks(self)
			elif self.input == '2':
				TodoApp.add_task(self)
			elif self.input == '3':
				TodoApp.delete_task(self)
			elif self.input == '4':
				TodoApp.save(self)
			elif self.input == 'c':
				TodoApp.clear(self)									
			elif self.input =='q':
				TodoApp.list_tasks(self)
				print('Goodbye', self.name)
				break 
					
if __name__=='__main__':
	app = TodoApp()
	print(help(app))
				
				
			
			
		
			
		
		
		
	
	