from order import OrderBook

class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split()
            workload = int(workload)
            self.order_book.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished_tasks(self):
        finished = self.order_book.finished_orders()
        if not finished:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def list_unfinished_tasks(self):
        unfinished = self.order_book.unfinished_orders()
        if not unfinished:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

    def mark_task_as_finished(self):
        try:
            task_id = int(input("id: "))
            self.order_book.mark_finished(task_id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")
        except Exception as e:
            print(e)

    def list_programmers(self):
        programmers = self.order_book.programmers()
        for programmer in programmers:
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            finished, unfinished, finished_hours, unfinished_hours = self.order_book.status_of_programmer(programmer)
            print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_hours} scheduled {unfinished_hours}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_task_as_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                print("erroneous input")
                self.help()



app = OrderBookApplication()
app.execute()