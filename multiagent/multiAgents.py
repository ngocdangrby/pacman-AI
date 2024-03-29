# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
    
from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        pacPos = currentGameState.getPacmanPosition()
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newGhostPos = successorGameState.getGhostPosition(1)
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # print(pacPos,newPos,successorGameState.getScore())
        # return successorGameState.getScore()
       
        foodList = currentGameState.getFood().asList()
        

            
        if len(foodList) > 0:
            score = 1.0/(min([manhattanDistance(newPos, foodPos) for foodPos in foodList])+5) + successorGameState.getScore()
        else:
            score = successorGameState.getScore()

        for index in range(len(newGhostStates)):
            dist_to_ghost = util.manhattanDistance(newPos, newGhostStates[index].getPosition())
            if dist_to_ghost <= 2 : return -200
        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        res = self.value(gameState, 0)
        return res[0]


    def value(self,state, depth):
        if  depth == self.depth * state.getNumAgents() or state.isWin() or state.isLose():
            return  (None, self.evaluationFunction(state))
        if(self.is_pacman_turn(state, depth)):
            return self.max_value(state, depth)
        else:
            return self.min_value(state, depth)

    def max_value(self, state, depth):
        actions = state.getLegalActions(0)
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))
        max_result = (None, -float('inf'))
        for action in actions:
            succ = state.generateSuccessor(0, action)
            res = self.value(succ, depth+1)
            if(res[1] > max_result[1]):
                    max_result = (action,res[1])
        return max_result

    def min_value(self, state, depth):
        actions = state.getLegalActions(self.get_agent_turn(state, depth))
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))

        min_result = (None, float('inf'))
        for action in actions:
            succ = state.generateSuccessor(self.get_agent_turn(state, depth), action)
            res = self.value(succ, depth+1)
            if(res[1] < min_result[1]):
                    min_result = (action,res[1])
        return min_result

    def is_pacman_turn(self, state, depth):
        return self.get_agent_turn(state, depth) == 0
    def get_agent_turn(self, state, depth):
        return depth % state.getNumAgents()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        res = self.value(gameState, 0,alpha= -float('inf'), beta=float('inf'))
        return res[0]


    def value(self,state, depth, alpha, beta):
        if  depth == self.depth * state.getNumAgents() or state.isWin() or state.isLose():
            return  (None, self.evaluationFunction(state))
        if(self.is_pacman_turn(state, depth)):
            return self.max_value(state, depth, alpha, beta)
        else:
            return self.min_value(state, depth, alpha, beta)

    def max_value(self, state, depth, alpha, beta):
        actions = state.getLegalActions(0)
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))
        v = (None, -float('inf'))
        for action in actions:
            succ = state.generateSuccessor(0, action)
            # v = max(v, self.value(succ, depth+1, alpha, beta), key=lambda x: x[1])
            res = self.value(succ, depth+1, alpha, beta)
            if res[1] > v[1]:
                v = (action, res[1])
            if(v[1] > beta):
                return v
            alpha = max(alpha,v[1])
        return v    

    def min_value(self, state, depth, alpha, beta):
        actions = state.getLegalActions(self.get_agent_turn(state, depth))
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))
        v = (None, float('inf'))
        for action in actions:
            succ = state.generateSuccessor(self.get_agent_turn(state, depth), action)
            v = min(v, self.value(succ, depth+1, alpha, beta), key=lambda x: x[1])
            if v[1] < alpha:
                return v
            beta = min(beta,v[1])
        return v

    def get_agent_turn(self, state, depth):
        return depth % state.getNumAgents()
    def is_pacman_turn(self, state, depth):
        return self.get_agent_turn(state, depth) == 0



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        res = self.value(gameState, 0)
        return res[0]


    def value(self,state, depth):
        if  depth == self.depth * state.getNumAgents() or state.isWin() or state.isLose():
            return  (None, self.evaluationFunction(state))
        if(self.is_pacman_turn(state, depth)):
            return self.max_value(state, depth)
        else:
            return self.exp_value(state, depth)

    def max_value(self, state, depth):
        actions = state.getLegalActions(0)
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))
        max_result = (None, -float('inf'))
        for action in actions:
            succ = state.generateSuccessor(0, action)
            res = self.value(succ, depth+1)
            if(res[1] > max_result[1]):
                    max_result = (action,res[1])
        return max_result

    def exp_value(self, state, depth):
        actions = state.getLegalActions(self.get_agent_turn(state, depth))
        if len(actions) == 0:
            return (None, self.evaluationFunction(state))

        exp_result = 0
        for action in actions:
            succ = state.generateSuccessor(self.get_agent_turn(state, depth), action)
            # print(succ)
            p = 1.0/float(len(actions))
            res = self.value(succ, depth+1)
            exp_result += p * res[1]
            result = (action, exp_result)
        return result


    def is_pacman_turn(self, state, depth):
        return self.get_agent_turn(state, depth) == 0
    def get_agent_turn(self, state, depth):
        return depth % state.getNumAgents()


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    ghostStates = currentGameState.getGhostStates()
    ghostPos = currentGameState.getGhostPosition(1)
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    pacPos = currentGameState.getPacmanPosition()

    foodList = currentGameState.getFood().asList()
    bigFoodList = currentGameState.getCapsules()
    score  = 0
   
    if len(bigFoodList) > 0:
        score += (1.0/(min([util.manhattanDistance(pacPos, bigFoodPos) for bigFoodPos in bigFoodList])+5))*200

    if len(ghostStates) > 0:
        for  x, ghostState in enumerate(ghostStates):
            if(scaredTimes[x] > 3):
                score += (1.0/(util.manhattanDistance(pacPos, ghostState.getPosition())+5))*1000
            else:
                dist_to_ghost = util.manhattanDistance(pacPos, ghostState.getPosition())
                if dist_to_ghost <= 2: return -1000

    if len(foodList) > 0:
        score += (1.0/(min([util.manhattanDistance(pacPos, foodPos) for foodPos in foodList])+5))*10

    return score + currentGameState.getScore()
# Abbreviation
better = betterEvaluationFunction

