"""
Class to implement the Publisher-Subscriber pattern
"""


class PubSub:
    def __init__(self):
        # Dictionary to hold lists of subscriber callbacks per event.
        self._subscribers = {}

    def subscribe(self, event, callback):
        """
        Subscribe to an event by adding a callback.

        Args:
            event (str): The name of the event.
            callback (callable): A function to be called when the event is published.
        """
        if event not in self._subscribers:
            self._subscribers[event] = []
        self._subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        """
        Unsubscribe a callback from an event.

        Args:
            event (str): The name of the event.
            callback (callable): The function to remove.
        """
        if event in self._subscribers:
            try:
                self._subscribers[event].remove(callback)
                # Remove event key if no subscribers remain.
                if not self._subscribers[event]:
                    del self._subscribers[event]
            except ValueError:
                pass  # The callback was not found

    def publish(self, event, *args, **kwargs):
        """
        Publish an event, triggering all subscriber callbacks for that event.

        Args:
            event (str): The name of the event.
            *args, **kwargs: Any arguments to pass to the callback functions.
        """
        if event in self._subscribers:
            for callback in list(self._subscribers[event]):
                callback(*args, **kwargs)


if __name__ == '__main__':
    # Create a PubSub instance
    pubsub = PubSub()

    # Define some subscriber callback functions
    def subscriber_one(data):
        print(f"Subscriber One received: {data}")

    def subscriber_two(data):
        print(f"Subscriber Two received: {data}")

    # Subscribe to an event named 'my_topic'
    pubsub.subscribe('my_topic', subscriber_one)
    pubsub.subscribe('my_topic', subscriber_two)

    # Publish 'my_topic' with some data
    pubsub.publish('my_topic', data="Hello, Pub/Sub!")

    # Unsubscribe subscriber_one and then publish the event again
    pubsub.unsubscribe('my_topic', subscriber_one)
    pubsub.publish('my_topic', data="Another message")
