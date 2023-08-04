SEARCH

AGENT = am entity that percieves its environemnt and is able to act on its environment

- EXAMPLE - represnted by a car on a gps taking tens following directions or finding the fasteds/best way

STATE = after an action happens it creates a new state. similar to react

INITITAL STATE = where you start.

ACTIONS = choices we can make in any given state

- define a func called actions that takes an input called S. Where S is going to be some state that exists inside our environement. - - Returns the output of all valid actions that can be taken.

- Action(s) return the set of actions that can be executed in state s

TRANSITION MODEL = a description of what state results from performing any applicable action in any state

- Result(s, a)
- returns the state resulting from performing action a in state s

STATE SPACE = the set of all state reachable from the intial state by any sequence of actions

GOAL STATE = some way to determine whether a given state is a goal state

PATH COST = numnerical cost associated with a given path

OPTIMAL SOLUTION = a solution that has the lowest path cost among all of the solutions

Actions(s)
Result(s, a)

Search problems have,

- inital state
- actions
- transition model
- goal test
- path cost func

NODE = a data structure that keeps track of

- a state
- an action(action applied to parent to node)
- a parent node that (generated this node)
- a path cost (from initial state to node)
