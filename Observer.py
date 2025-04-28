from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, new_state):
        pass

class DeviceStateManager:
    def __init__(self):
        self._observers = []
        self._state = None

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        print(f"Device changing state to: {state}")
        self._state = state
        self._notify_observers()

    def get_state(self):
        return self._state


class Logger(Observer):
    def update(self, new_state):
        print(f"[Logger] Device changed to state: {new_state}")

class Monitor(Observer):
    def update(self, new_state):
        print(f"[Monitor] Monitoring device now in state: {new_state}")

class Alarm(Observer):
    def update(self, new_state):
        if new_state == "فعال":
            print("[Alarm] دستگاه فعال شد! آلارم آماده به کار.")
        elif new_state == "غیرفعال":
            print("[Alarm] دستگاه خاموش شد. آلارم غیر فعال.")


if __name__ == "__main__":
    device_manager = DeviceStateManager()

    logger = Logger()
    monitor = Monitor()
    alarm = Alarm()

    device_manager.add_observer(logger)
    device_manager.add_observer(monitor)
    device_manager.add_observer(alarm)

    device_manager.set_state("فعال")
    device_manager.set_state("استراحت")
    device_manager.set_state("غیرفعال")
