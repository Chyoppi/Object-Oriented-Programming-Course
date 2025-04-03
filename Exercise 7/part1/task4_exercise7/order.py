from task import Task

class OrderBook:
    def __init__(self):
        self.orders = []
    
    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set(task.programmer for task in self.orders))
    
    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"No task with ID {id} exists.")
            
    def finished_orders(self):
        return [task for task in self.orders if task.progress]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.progress]
    
    def status_of_programmer(self, programmer: str):
        finished_tasks = [task for task in self.orders if task.programmer == programmer and task.progress]
        unfinished_tasks = [task for task in self.orders if task.programmer == programmer and not task.progress]

        finished_count = len(finished_tasks)
        unfinished_count = len(unfinished_tasks)
        finished_workload = sum(task.workload for task in finished_tasks)
        unfinished_workload = sum(task.workload for task in unfinished_tasks)

        return (finished_count, unfinished_count, finished_workload, unfinished_workload)

    
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)