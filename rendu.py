import datetime, time
import operator


class Task:
	
	def __init__(self, NAME, PERIOD, EXECUTION_TIME, COOLDOWN, MATERIALMADE = 0, PRIORITY = 0, OILNEED = 0) :
		self.NAME = NAME
		self.PERIOD = PERIOD
		self.EXECUTION_TIME = EXECUTION_TIME
		self.COOLDOWN = COOLDOWN 
		self.PRIORITY = PRIORITY		# 0 by default
		self.MATERIALMADE = MATERIALMADE 
		self.LAST_EXECUTED_TIME = datetime.datetime.now()

	def run(self):

		global timer
		print(str(timer) + "\t=> " + self.NAME + " started.")
		time.sleep(self.EXECUTION_TIME)
		print(str(timer) + "\t=> " + self.NAME + " finished.")
		self.COOLDOWN = self.PERIOD
		if current_task.MATERIALMADE == 20:
			current_task.PRIORITY == 4
		
if __name__ == "__main__":

	# Definition of all tasks and instanciation
	task_list  = [
		Task(NAME = 'Pump1', PERIOD = 5, EXECUTION_TIME = 2, COOLDOWN = 0, MATERIALMADE = 10, PRIORITY = 2),
		Task(NAME = 'Pump2', PERIOD =  15, EXECUTION_TIME = 3, COOLDOWN = 0, MATERIALMADE = 20, PRIORITY = 1),
		Task(NAME  = 'Machine1', PERIOD = 5, EXECUTION_TIME = 5, COOLDOWN = 0, MATERIALMADE = 0, PRIORITY = 3, OILNEED = 25),
		Task(NAME = 'Machine2', PERIOD = 5, EXECUTION_TIME = 3, COOLDOWN = 0, MATERIALMADE = 0, PRIORITY = 4, OILNEED = 5)]

	global timer
	timer = -1
	global tank

	# Global scheduling loop
	while(True) :

		task_to_run = None
		task_priority = 0
		motors = 0
		wheels = 0
		engines = 0
		tank = 0
		oil = 0
		timer += 1
		
		for current_task in task_list:

			current_task_next_deadline = current_task.EXECUTION_TIME + current_task.PERIOD

			print("\tDeadline for task " + current_task.NAME + " : " + str(current_task_next_deadline))
			
			while current_task.PRIORITY == 1:

				if current_task.NAME  == "Pump1":
					current_task = task_to_run
					if oil == 0 :
						task_to_run.PRIORITY = 1
					if oil > 0 and oil < 26:
						task_to_run.PRIORITY = 2
					if oil > 25 and oil < 50:
						task_to_run.PRIORITY = 3
					if oil == 50:
						task_to_run.PRIORITY = 4
						
					if operator.ge(datetime.datetime.now() + datetime.timedelta(0, task_to_run.PERIOD)) and task_to_run.PRIORITY != 4:
						if task_to_run.PRIORITY == 1:
							oil += 10
							time.sleep(task_to_run.EXECUTION_TIME)
							task_to_run.LAST_EXECUTED_TIME = datetime.datetime.now()
						if task_to_run.PRIORITY == 2:
							oil += 10
							time.sleep(task_to_run.EXECUTION_TIME)  
							task_to_run.LAST_EXECUTED_TIME = datetime.datetime.now()    
							
						if oil > 50:
							oil = oil - (oil - 50)
						print(task_to_run.LAST_EXECUTED_TIME.strftime("%H:%M:%S") +" :" + task_to_run.NAME + ": add 10 oil in tank. Tank have now " + str(oil) + " oil")
				if current_task.NAME  == "Pump2":
					if oil == 0 :
						task_to_run.PRIORITY = 1
					if oil > 0 and oil < 26:
						task_to_run.PRIORITY = 2
					if oil > 25 and oil < 50:
						task_to_run.PRIORITY = 3
					if oil == 50:
						task_to_run.PRIORITY = 4
						
					if operator.ge(datetime.datetime.now() + datetime.timedelta(0, task_to_run.PERIOD)) and task_to_run.PRIORITY != 4:
						if task_to_run.PRIORITY == 1:
							oil += 10
							time.sleep(task_to_run.EXECUTION_TIME)
							task_to_run.LAST_EXECUTED_TIME = datetime.datetime.now()
						if task_to_run.PRIORITY == 2:
							oil += 10
							time.sleep(task_to_run.EXECUTION_TIME)  
							task_to_run.LAST_EXECUTED_TIME = datetime.datetime.now()    
							
						if oil > 50:
							oil = oil - (oil - 50)
						print(task_to_run.LAST_EXECUTED_TIME.strftime("%H:%M:%S") +" :" + task_to_run.NAME + ": add 10 oil in tank. Tank have now " + str(oil) + " oil")
				if current_task.NAME == 'Machine1' and (wheels/4)>motors:
					motors += 1
					task_to_run = current_task
				if current_task.NAME == 'Machine2' and (wheels/4)<motors:
					wheels += 1
					task_to_run = current_task


		# Start task selected by scheduler
		# task_to_run.run()

		# Choose the task to be run
		for current_task in task_list  :	
				
			if current_task.NAME == 'Pump1' or current_task.NAME == 'Pump2':
				if tank + current_task.MATERIALMADE >= 50:
					current_task.PRIORITY = 5
			
			current_task.COOLDOWN - 1

			if current_task.PRIORITY < task_to_run.PRIORITY and current_task.COOLDOWN <= 0:
				task_to_run = current_task
					
		
		if task_to_run == None :
			time.sleep(1)
			print(str(timer) + "\tIdle")
		else :
			task_to_run.run()
