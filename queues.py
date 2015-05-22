from itertools import accumulate, islice
import random


class Item:
    def __init__(self,
                 arrival_time,
                 processing_time,
                 enqueue_time):
        self.arrival_time = arrival_time
        self.processing_time = processing_time
        self.enqueue_time = enqueue_time

    @property
    def dequeue_time(self):
        return self.enqueue_time + self.processing_time

    def __repr__(self):
        return 'Item(arr={}, proc={}, enq={}, deq={})'.format(
            self.arrival_time,
            self.processing_time,
            self.enqueue_time,
            self.dequeue_time)


def exponential_seq(mean):
    while True:
        yield random.expovariate(1.0 / mean)


def work_items(arrival_intervals, processing_times):
    arrival_times = accumulate(arrival_intervals)
    previous_item = None
    for at, pt in zip(arrival_times, processing_times):
        if previous_item is None:
            previous_item = Item(at, pt, at)
            yield previous_item
        else:
            enqueue_time = max(previous_item.dequeue_time, at)
            previous_item = Item(at, pt, enqueue_time)
            yield previous_item
