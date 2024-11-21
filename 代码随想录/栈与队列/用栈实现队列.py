class MyQueue:
    def __init__(self):
        self.stack_in = [int]
        self.stack_out = [int]

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
