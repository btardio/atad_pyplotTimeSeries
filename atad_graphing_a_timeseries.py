
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import matplotlib.dates

# clear axis
plt.cla()

# clear figure
plt.clf()


# get the current time
now = datetime.utcnow().timestamp()

# create a list of datetime objects from 'n days past' to yesterday
def createdayseries(n):

    # 86400 is the number of seconds in a day
    # np.floor is using only the year/month/day part of date2num which also has an hour/minute/second/... part
    # matplotlib.dates.date2num converts a DateTime object to a matplotlib number
    # datetime.fromtimestamp creates a DateTime object given an integer of seconds lapsed since epoch
    days = [np.floor(matplotlib.dates.date2num(datetime.fromtimestamp( now - (x * 86400) ) ) ) for x in range(n+1,1,-1)]

    return days


days = createdayseries(7)

# get the current figure
fig = plt.gcf()

# get the current axes
axes = plt.gca()

# disable autoscaling
axes.autoscale(enable=False, axis='both')


# x axis

axes.set_xticklabels([matplotlib.dates.num2date(x).date() for x in days])

axes.set_xticks(days)

axes.set_xbound(days[0], days[-1])

axes.tick_params(axis='x', direction='inout', rotation=45, grid_alpha=0.75, grid_linewidth=2)

axes.grid(b=True, axis='x')



# y axis

axes.set_yticklabels([0,1,2,3,4,5,6,7])

axes.set_yticks([0,1,2,3,4,5,6,7])

axes.set_ybound(0, 7)

axes.tick_params(axis='y', direction='inout', rotation=45, grid_alpha=0.75, grid_linewidth=2)

axes.grid(b=True, axis='y')



# do plotting

plt.plot(days,[1,2,1,4,5,6,7])

plt.show()


# Note: This could be another method for graphing dates, but this example is using numbers and not DateTime objects
# axes.xaxis_date()


