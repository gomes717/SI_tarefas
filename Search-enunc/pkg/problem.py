from maze import Maze
from state import State
from cardinal import *

class Problem:
    """Representação de um problema a ser resolvido por um algoritmo de busca clássica.
    A formulação do problema - instância desta classe - reside na 'mente' do agente."""


    def __init__(self):
        self.initialState = State(0,0)
        self.goalState = State(0,0)

    def createMaze(self, maxRows, maxColumns):
        """Este método instancia um labirinto - representa o que o agente crê ser o labirinto.
        As paredes devem ser colocadas fora desta classe porque este.
        @param maxRows: máximo de linhas do labirinto.
        @param maxColumns: máximo de colunas do labirinto."""
        self.mazeBelief = Maze(maxRows, maxColumns)
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.cost = [[0.0 for j in range(maxRows*maxColumns)]for i in range(8)]

    def defInitialState(self, row, col):
        """Define o estado inicial.
        @param row: linha do estado inicial.
        @param col: coluna do estado inicial."""
        self.initialState.row = row
        self.initialState.col = col

    def defGoalState(self, row, col):
        """Define o estado objetivo.
        @param row: linha do estado objetivo.
        @param col: coluna do estado objetivo."""
        self.goalState.row = row
        self.goalState.col = col

    def suc(self, state, action):
        """, sucessor ao executar uma ação.
        @param state: estado atual.
        @param action: ação a ser realizado a partir do estado state.
        @return estado sucessor"""
        row = state.row
        col = state.col

        # @TODO T_AAFP

        return State(row, col)

    def possibleActions(self, state):
        """Retorna as ações possíveis de serem executadas em um estado.
        O valor retornado é um vetor de inteiros.
        Se o valor da posição é -1 então a ação correspondente não pode ser executada, caso contrário valerá 1.
        Exemplo: se retornar [-1, -1, -1, 1, 1, -1, -1, -1] apenas as ações 3 e 4 podem ser executadas, ou seja, apenas SE e S.
        @param state: estado atual.
        @return ações possíveis"""

        actions = [1,1,1,1,1,1,1,1] # Supõe que todas as ações são possíveis
        # @TODO T_AAFP

        row = state.row
        col = state.col
        #testa final do mapa
        if(col+1 >= self.maxColumns):
            actions[1] = actions[2] = actions[3] = -1
        elif(col-1 < 0):
            actions[5] = actions[6] = actions[7] = -1
        if(col+1 < self.maxColumns):
            if(self.mazeBelief.walls[row][col + 1]): #L
                actions[2] = -1
        if(col-1 >= 0):
            if(self.mazeBelief.walls[row][col - 1]): #O
                actions[6] = -1
        if(row+1 >= self.maxRows):
            actions[3] = actions[4] = actions[5] = -1
        elif(row-1 < 0):
            actions[0] = actions[1] = actions[7] = -1
        if(row-1 >= 0):
            if(self.mazeBelief.walls[row - 1][col]): #N
                actions[0] = -1
            if(col-1 >= 0):
                if(self.mazeBelief.walls[row -1][col-1]): #NO
                    actions[7] = -1
            if(col + 1 < self.maxColumns):
                if(self.mazeBelief.walls[row - 1][col+1]): #NE
                    actions[1] = -1
        if(row+1 < self.maxRows):
            if(self.mazeBelief.walls[row + 1][col]): #S
                    actions[4] = -1
            if(col - 1 >= 0):
                if(self.mazeBelief.walls[row + 1][col-1]): #SO
                    actions[5] = -1
            if(col +1 < self.maxColumns):
                if(self.mazeBelief.walls[row + 1][col+1]): #SE
                    actions[3] = -1

        return actions

    def possibleActionsWithoutCollaterals(self, state):
        """Retorna as ações possíveis de serem executadas em um estado, desconsiderando movimentos na diagonal.
        O valor retornado é um vetor de inteiros.
        Se o valor da posição é -1 então a ação correspondente não pode ser executada, caso contrário valerá 1.
        Exemplo: se retornar [1, -1, -1, -1, -1, -1, -1, -1] apenas a ação 0 pode ser executada, ou seja, apena N.
        @param state: estado atual.
        @return ações possíveis"""

        actions = [1,-1,1,-1,1,-1,1,-1] # Supõe que todas as ações (menos na diagonal) são possíveis

        # @TODO T_AAFP
        if(col+1 >= self.maxColumns):
             actions[2] = -1
        elif(col-1 < 0):
             actions[6] = -1

        if(col+1 < self.maxColumns):
            if(self.mazeBelief.walls[row][col + 1]): #L
                actions[2] = -1
        if(col-1 >= 0):
            if(self.mazeBelief.walls[row][col - 1]): #O
                actions[6] = -1

        if(row+1 >= self.maxRows):
            actions[4] = -1
        elif(row-1 < 0):
            actions[0] = -1

        if(row-1 >= 0):
            if(self.mazeBelief.walls[row - 1][col]): #N
                actions[0] = -1
        if(row+1 < self.maxRows):
            if(self.mazeBelief.walls[row + 1][col]): #S
                actions[4] = -1


        return actions

    def getActionCost(self, action):
        """Retorna o custo da ação.
        @param action:
        @return custo da ação"""
        if (action == N or action == L or action == O or action == S):
            return 1.0
        else:
            return 1.5

    def goalTest(self, currentState):
        """Testa se alcançou o estado objetivo.
        @param currentState: estado atual.
        @return True se o estado atual for igual ao estado objetivo."""
         # @TODO T_AAFP
        return True # Utilizar Operador de igualdade definido em __eq__ no arquivo state.py
