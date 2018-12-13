# Tutorial: Graph a time series with matplotlib

In this tutorial we will be using bounds, ticks and tick labels to produce a simple time series graph. This tutorial is fairly short and simple, but using the structure shown will allow us to graph most if not any data with greater flexibility.


## Code

```python

%matplotlib inline

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


```

## Conclusion

There are a lot of features within matplotlib, and separating features into manageable components can be challenging. Organization of code can lessen the frustration and in this tutorial we presented a simple organization technique for manipulating how the x and y axes are shown.

Because matplotlib acts as a graphics rendering state machine we can easily move the code that manipulates the axes into a function without having to pass in or return the current axes or current figure. This also has its drawbacks. Not recognizing the progression of states could lead to setting and resetting states. This fact makes it even more important to organize and modularize.

Further information about finite state machines: <https://en.wikipedia.org/wiki/Finite-state_machine>.

