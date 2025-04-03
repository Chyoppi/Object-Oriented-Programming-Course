from random import randint

class Task:
    next_id = 1

    def __init__(self, description:str, programmer:str, workload:int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.progress = False
        self.id = Task.next_id
        Task.next_id += 1 

    def mark_finished(self):
        self.progress = True
        print(f"Task {self.description} is finished.")

    def  is_finished(self):
        if self.progress:
            return "IS FINISHED"
        else:
            return "NOT FINISHED"
    
    def __str__(self):
        return f"{self.id}: {self.description}, programmer {self.programmer}, Workload: {self.workload} hourse, {self.is_finished()}"
