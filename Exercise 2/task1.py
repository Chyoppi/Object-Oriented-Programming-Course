queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

# The first person in the queue leaves after paying for their purchases
time1 = queue.pop(0)
print(queue)

# Ville recruits Anni to queue on his behalf
time2 = queue.pop(-2)
time2 = queue.insert(-1, "Anni")
print(queue)

# Jarno leaves, tired of the constant waiting
time3 = queue.pop(-1)
print(queue)

# Marjo joins the end of the queue
time4 = queue.append("Marjo")
print(queue)

# Antti lets two people behind him go ahead of him
time5 = queue.pop(1)
time5 = queue.insert(3, "Antti")
print(queue)

#Is Jenni in the queue? If so, at what position? And who is the third last personin the queue?

print(f"{queue[1]} is second one in the queue and the third last person is {queue[-3]}")
