from abc import ABC, abstractmethod

class ElevatorState(ABC):
    @abstractmethod
    def handle_request(self, elevator, request_floor):
        pass

    @abstractmethod
    def arrive(self, elevator):
        pass


class MovingUpState(ElevatorState):
    def handle_request(self, elevator, request_floor):
        print(f"[UP] Already moving. Added floor {request_floor} to queue.")
        elevator.add_request(request_floor)

    def arrive(self, elevator):
        elevator.current_floor += 1
        print(f"[UP] Arrived at floor {elevator.current_floor}")
        if elevator.current_floor == max(elevator.requests_up, default=elevator.current_floor):
            elevator.requests_up.clear()
            elevator.set_state(IdleState())
        else:
            elevator.process_next_request()

class MovingDownState(ElevatorState):
    def handle_request(self, elevator, request_floor):
        print(f"[DOWN] Already moving. Added floor {request_floor} to queue.")
        elevator.add_request(request_floor)

    def arrive(self, elevator):
        elevator.current_floor -= 1
        print(f"[DOWN] Arrived at floor {elevator.current_floor}")
        if elevator.current_floor == min(elevator.requests_down, default=elevator.current_floor):
            elevator.requests_down.clear()
            elevator.set_state(IdleState())
        else:
            elevator.process_next_request()

class IdleState(ElevatorState):
    def handle_request(self, elevator, request_floor):
        print(f"[IDLE] Received request to floor {request_floor}")
        elevator.add_request(request_floor)
        if request_floor > elevator.current_floor:
            elevator.set_state(MovingUpState())
        elif request_floor < elevator.current_floor:
            elevator.set_state(MovingDownState())
        else:
            print("[IDLE] Already at requested floor.")

    def arrive(self, elevator):
        print("[IDLE] No movement needed.")


class Elevator:
    def __init__(self, min_floor=0, max_floor=10):
        self.state = IdleState()
        self.current_floor = 0
        self.requests_up = []
        self.requests_down = []
        self.min_floor = min_floor
        self.max_floor = max_floor

    def set_state(self, state):
        print(f"Changing state to {state.__class__.__name__}")
        self.state = state
        self.process_next_request()

    def add_request(self, floor):
        if floor > self.current_floor:
            if floor not in self.requests_up:
                self.requests_up.append(floor)
                self.requests_up.sort()
        elif floor < self.current_floor:
            if floor not in self.requests_down:
                self.requests_down.append(floor)
                self.requests_down.sort(reverse=True)

    def request(self, floor):
        if floor < self.min_floor or floor > self.max_floor:
            print(f"[ERROR] Floor {floor} is out of range!")
            return
        self.state.handle_request(self, floor)

    def process_next_request(self):
        if isinstance(self.state, MovingUpState) and self.requests_up:
            next_floor = self.requests_up[0]
            if self.current_floor < next_floor:
                self.state.arrive(self)
        elif isinstance(self.state, MovingDownState) and self.requests_down:
            next_floor = self.requests_down[0]
            if self.current_floor > next_floor:
                self.state.arrive(self)


if __name__ == "__main__":
    elevator = Elevator(min_floor=0, max_floor=5)
    elevator.request(3)
    elevator.request(1)
    elevator.request(5)
