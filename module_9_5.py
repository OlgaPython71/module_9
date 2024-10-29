class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.step = step
        self.start = start
        self.stop = stop
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()
        return self.pointer
