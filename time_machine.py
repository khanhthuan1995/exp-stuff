class TimeMachine():
    def __init__(self, current_time=1) -> None:
        
        self.current_time = current_time
    def set_next(self) -> None:
        self.current_time+=1
    def back_in_time(self) -> None:
        pass


time_machine = TimeMachine()
time_machine.set_next()
time_machine.current_time


