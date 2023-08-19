import matplotlib.pyplot as plt

time = []
status = []
tracking = open("D:\\Code\\Python\\tracking.txt", "r")
token = tracking.read().split()
token.pop(0)        # Remove first element because it's content not data of statistics
for item in token:
    if len(item) == 1: status.append(int(item))
    else: time.append(item)
tracking.close()
fig = plt.figure()
fig.set_figheight(30)
fig.set_figwidth(300)
plt.plot(time, status)
plt.savefig("D:\\Code\\Python\\figure.jpg", bbox_inches = 'tight')

