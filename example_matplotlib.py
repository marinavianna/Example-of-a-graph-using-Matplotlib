from matplotlib import pyplot as plt

years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
margarine = [3.7,3.2,2.9,2.4,2.3,1.8,2.1,2.1,1.9,1.7]
divorce = [5,4.7,4.6,4.4,4.3,4.1,4.2,4.2,4.2,4.1]

fig, plot1 = plt.subplots()
plot2 = plot1.twinx()

plot1.plot(years,margarine, color = 'pink', marker = 'o')
plot2.plot(years,divorce, color = 'gray', marker = 'o')

fig.suptitle('Divorce rate in Maine \n correlates with \n Per capita consumption of margarine')
plot1.set_xlabel('Years')
plot1.set_ylabel('Per capita consumption of margarine (kg)')
plot2.set_ylabel('Divorce rate in Maine per 1,000')
fig.legend(['Margarine consumption', 'Divorce rate'], loc="upper right", bbox_to_anchor=(1,1), bbox_transform=plot1.transAxes)

fig.subplots_adjust(top=0.85)

plt.show()