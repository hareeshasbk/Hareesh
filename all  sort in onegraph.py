import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

x=list(range(1,10))
plt.plot(x ,[y*y for y in x], color = 'orange')
plt.plot(x ,[y for y in x], color = 'red')
plt.plot(x ,[y*y for y in x], color = 'blue')
plt.title("Bubble sort- time complexity is O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()

