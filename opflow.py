class Opflow:

    def __init__(self):
        self.operator_flow = []

    def push(self, operator):
        operator_flow = self.operator_flow
        operator_flow.append(operator)
        return operator_flow

    def pop(self):
        operator_flow = self.operator_flow
        operator_flow.pop()
        return operator_flow

    def access_state(self):
        # operator_flow = self.operator_flow
        pass

