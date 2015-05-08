# Simulate a car lot.
#
# Manager wants to maintain a specific number of cars on the lot. On a
# given day a certain number are purchased and a given number
# arrive. The number purchased will be random around some average. The
# number to arrive will be the number ordered by the manager D days
# ago, where D is the delivery delay.
#
# The interest element is how the manager decides how many to order on
# a given day. The numbers they can use to calculate this are:
#
#  - rate of car sales over some time span (1 day, 3 days, forever)
#  - the percentage of the calculated average that they purchase on a
#    given day.
#
# If D were zero, obviously the manager could just order the number of
# cars sold each day. With delay, however, the manager runs the risk
# of over- or under-purchasing when there are transient spikes or dips
# in demand.
#
# For given set of parameters, plot the actual number of cars on the
# lot each day.

from collections import deque


def purchase_order(stock, target):
    """Calculate the next purchase order.
    """
    five_day_avg = sum(stock[-5:]) / min(5, len(stock))
    diff = max(target - five_day_avg, 0)
    return int(diff / 3)


def sales():
    """Determine the number of cars sold on a given day.
    """
    return 5


def simulate(target_stock=200, num_days=1000, delivery_delay=5):
    stock = [200]
    purchase_orders = deque([0] * delivery_delay)

    for day in range(num_days):
        new_stock = stock[-1] - sales()
        new_stock += purchase_orders.popleft()
        stock.append(new_stock)
        purchase_orders.append(purchase_order(stock, target_stock))

    return stock

print(simulate())
