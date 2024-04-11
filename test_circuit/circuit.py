import math
import queue
from typing import List, Tuple, Optional


class Gate:
    """Logical representation of a single gate
    """

    target: int
    control: int
    target_state: int
    control_state: int
    inc_or_dec: str
    tq: str  # ternary or quaternary

    def __init__(self, target: int, control: int, target_state: int, control_state: int, inc_or_dec: str, tq: str):
        """
        Args:
            target (int): target of the gate
            control (int): control of the gate
            target_state (int): state of the target
            control_state (int): state of the control
            inc_or_dec (str): whether this is an incementer or a decrementer (+/-)
            tq (str): ternary or quaternary gate
        """
        self.target = target
        self.control = control
        self.target_state = target_state
        self.control_state = control_state
        self.inc_or_dec = inc_or_dec
        self.tq = tq

    def flip(self):
        """Flips the gate, from incrementer to a decrementer

        Returns:
            Gate: new Gate with inc_or_dec set to decrement(-)
        """
        return Gate(self.target, self.control, self.target_state, self.control_state, "-", self.tq)

    def __str__(self) -> str:
        return f"{self.tq} | target node: {self.target} state: {self.target_state} | control node: {self.control} state: {self.control_state} -> {self.inc_or_dec}"


class Q:
    """A Queue Data structure
    """
    def __init__(self):
        self.queue = queue.Queue()

    def enqueue(self, item: int) -> None:
        self.queue.put(item)

    def dequeue(self) -> int:
        return self.queue.get()

    def is_empty(self) -> bool:
        return self.queue.empty()

    def is_not_empty(self) -> bool:
        return not self.queue.empty()

    def size(self) -> int:
        return self.queue.qsize()

    def enqueue_children(self, parent: int) -> None:
        self.queue.put(parent * 2)
        self.queue.put(parent * 2 + 1)


class Circuit:
    """Representation of a circuit comprising of multiple Gate objects
    """
    n: int
    c: int
    q: Q
    gpll: int
    quat: int
    tern: int
    levels: List[List[Tuple[Optional[Gate], Optional[Gate]]]]
    final_levels: List[List[Tuple[Optional[Gate], Optional[Gate]]]]

    depth: int

    qubits: set[int]
    qutrits: set[int]
    ququads: set[int]

    # maps node number of a binary tree with left to right in-order traversal numbers
    # {8: 0, 4: 1, 2: 2, 5: 3, 1: 4, 6: 5, 3: 6, 7: 7, 9: 8}
    actual_mapping: dict

    def __init__(self, noOfLines: int):
        """

        Args:
            noOfLines (int): number of inputs lines to the entire circuit
        """
        self.n = noOfLines
        self.c = self.n - 1  # number of controls
        self.q = Q() # queue
        self.depth = (math.floor(math.log(self.c, 2)))
        self.levels = [[] for _ in range(0, self.depth)]

        self.quat = 0 # quaternary gates
        self.tern = 0 # ternary gates
        self.gpll: int = self.c // 4  # GrandParent of Last element of Last level

        self.qubits = set()
        self.qutrits = set()
        self.ququads = set()
        self.actual_mapping = self.inorder_traversal()

    def check_id(self, node_index: int) -> bool:
        """Check if this is an immediate decomposition

        Args:
            node_index (int): index for node of the binary tree

        Returns:
            bool: true / false
        """
        return node_index > self.gpll

    def check_gpll(self, node_index: int) -> bool:
        """Check if this is a grandparent of the last element of the last level

        Args:
            node_index (int): index for the node of the binary tree

        Returns:
            bool: true / false
        """
        return node_index == self.gpll

    def gpll_has_right_grandchild(self) -> bool:
        """Check if the node that is the grandparent of the last element of the last level has a right child or not

        Returns:
            bool: true / false
        """
        if (2 * (self.c // 2)) - (4 * (self.c // 4)) == 2:  # right grandchild present
            return True
        return False

    def check_sd(self, node_index: int) -> bool:
        """Check if the node will be a part of a subsequent decomposition

        Args:
            node_index (int): index for the node of the binary tree

        Returns:
            bool: true / false
        """
        return node_index < self.gpll

    def simulate(self):

        self.qutrits.add(1)
        self.qubits.add(self.n)

        # print(self.depth)
        self.q.enqueue(1)
        current_depth = -1

        while self.q.is_not_empty():
            # 1. check if this is a parent of an Immediate Decomposition:
            #       1. this is a part of an ID, then don't enqueue the children.
            #       2. count the number of qubits and qutrits that will be used up.
            #       3. count the number of ternary and quaternary gates that are required.

            # 2. check if this element is a gpll:
            #       1. observe if this has any right grandchildren
            #       2. enqueue the children
            #       3. count ququads (if any) and qutrits
            #       4. count the ternary and quaternary gates that are required.

            # 3. check if this element is a part of a Subsequent Decomposition:
            #       1. enqueue this node's children
            #       2. count the number of ququads and qutrits
            #       3. count the ternary and quaternary gates that would be required for this decomposition
            #       4. count the ququads and qutrits

            # NOTE: don't forget to consider the qutrit for the root of the tree which is 1

            current_node: int = self.q.dequeue()

            if current_node == 1 << (current_depth + 1):
                current_depth += 1

            # left and right childrens
            left_node = current_node * 2
            right_node = current_node * 2 + 1

            index = self.depth - 1 - current_depth
            decomposition = []

            # print("---")
            condition, stage = None, None

            if self.check_id(current_node):

                # check if current node even has a right child
                if right_node > self.c:
                    # print(f'Ternary CNOT gate with control: {left_node}, target: {current_node}')

                    # decomposition = self.make_gates(left_node, current_node, right_node, True, "id")
                    self.tern += 1 + 1

                    self.qubits.add(left_node)

                else:
                    # print(f'Ternary CNOT gate with control: {left_node}, target: {right_node}')
                    # print(f'Ternary CNOT gate with control: {right_node}, target: {current_node}')
                    # decomposition = self.make_gates(left_node, current_node, right_node, False, "id")
                    self.tern += 2 + 2

                    self.qubits.add(left_node)
                    self.qutrits.add(right_node)

                condition = right_node > self.c
                stage = "id"

                # store the left and right child

            elif self.check_gpll(current_node):
                # check if the gpll has a right grandchild
                # if it has we use 2 ternary gates else 2 quaternary
                if self.gpll_has_right_grandchild():
                    # print(f'Quaternary CNOT gate with control: {left_node}, target: {right_node}')
                    # print(f'Quaternary CNOT gate with control: {right_node}, target: {current_node}')

                    # decomposition = self.make_gates(left_node, current_node, right_node, True, "gpll")

                    self.quat += 2 + 2
                    self.q.enqueue_children(current_node)

                    self.qutrits.add(left_node)
                    self.ququads.add(right_node)

                else:
                    # print(f'Ternary CNOT gate with control: {left_node}, target: {right_node}')
                    # print(f'Ternary CNOT gate with control: {right_node}, target: {current_node}')

                    # decomposition = self.make_gates(left_node, current_node, right_node, False, "gpll")

                    self.tern += 2 + 2
                    self.q.enqueue(left_node)  # no point in enqueueing the right child if it has no children of its own

                    self.qutrits.add(left_node)
                    self.qutrits.add(right_node)

                condition = self.gpll_has_right_grandchild
                stage = "gpll"

                current_depth += 1  # to keep GPLL on a different level

            elif self.check_sd(current_node):
                # print(f'Quaternary CNOT gate with control: {left_node}, target: {right_node}')
                # print(f'Quaternary CNOT gate with control: {right_node}, target: {current_node}')

                # decomposition = self.make_gates(left_node, current_node, right_node, True, "sd")

                self.quat += 2 + 2
                self.q.enqueue_children(current_node)

                self.qutrits.add(left_node)
                self.ququads.add(right_node)

                stage = "sd"

            decomposition = self.make_gates(left_node, current_node, right_node, condition, stage)
            self.levels[index].append(decomposition)

        self.tern += 1  # this is for incorporating the target qubit

        # self.final_levels = [[] for _ in range(2 * len(self.levels) + 1)]

        """while front <= back:
            if front == back:
                print("Front = Back = ", front)
                self.final_levels[front].append((Gate(self.n, 1, 1, 2, "$", "Ternary"), None))
                # root decomposition
                break

            current_level = self.levels[front]
            self.final_levels[front] = self.levels[front]

            temp_decomp = []

            for decomp in current_level:
                left, right = decomp
                left = left.flip()
                if right is not None:
                    right = right.flip()
                temp_decomp.append((right, left))

            self.final_levels[back] = temp_decomp

            front += 1
            back -= 1"""
        
        gate_involving_main_target = [[(Gate(self.n, 1, 1, 2, "$", "Ternary"), None)]]
        reflection = self.get_reflection(self.levels)

        self.final_levels = self.levels + gate_involving_main_target + reflection # list of list of gates   

    def get_reflection(self, levels: List[List[Tuple[Optional[Gate], Optional[Gate]]]]):
        """Think of this like reflecting a binary tree about it's root node and having the gates flipped (+ becomes -)

        Args:
            levels (List[List[Tuple[Optional[Gate], Optional[Gate]]]]): List of levels, each level contains multiple gate pairs

        Returns:
            _type_: reflected list of levels with gates flipped
        """

        rev_levels = []

        for level in reversed(levels):
            temp_decomp = []

            for decomp in level:
                left, right = decomp
                left = left.flip()
                if right is not None:
                    right = right.flip()

                temp_decomp.append((right, left)) # reverse order

            rev_levels.append(temp_decomp)

        return rev_levels

    def make_gates(self, left, center, right, condition: bool, stage: str) -> Tuple[Optional[Gate], Optional[Gate]]:
        match stage:
            case "id":
                if condition:  # no right supplied
                    return (Gate(center, left, 2 + 1, 2 - 1, "+", "Ternary"),
                            None)
                else:
                    return (Gate(right, left, 2 + 1, 2 - 1, "+", "Ternary"),
                            Gate(center, right, 2 + 1, 2, "+", "Ternary"))
            case "gpll":
                # print("GPLL HERE: ", right, left)
                if condition:
                    return ((Gate(right, left, 2 + 2, 2, '+', "Quaternary"),
                             Gate(center, right, 2 + 1, 2 + 1, '+', "Quaternary")))
                else:
                    return (Gate(right, left, 2 + 1, 2, '+', "Ternary"),
                            Gate(center, right, 2 + 1, 2, '+', "Ternary"))
            case "sd":
                return (Gate(right, left, 2 + 2, 2, '+', "Quaternary"),
                        Gate(center, right, 2 + 1, 2 + 1, '+', "Quaternary"))

    def inorder_traversal(self):
        def generate_inorder(parent):
            if parent > self.c:
                return []

            left = parent * 2
            right = parent * 2 + 1

            return generate_inorder(left) + [parent] + generate_inorder(right)

        order = generate_inorder(1)

        mapping = {elem: index for index, elem in enumerate(order)}
        mapping[self.n] = self.n - 1

        # print(mapping)

        return mapping
