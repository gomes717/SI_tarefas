from model import Model
from problem import Problem
from state import State
from cardinal import action
from tree import TreeNode


class Agent:
    """"""
    counter = -1 # Contador de passos no plano, usado na deliberação

    def __init__(self, model):
        """Construtor do agente.
        @param model: Referência do ambiente onde o agente atuará."""
        self.model = model

        self.prob = Problem()
        # @TODO T_AAFP - criar crencas sobre as paredes do labirinto
        self.prob.createMaze(9, 9)
        self.prob.mazeBelief.putVerticalWall(0,1,0)
        self.prob.mazeBelief.putVerticalWall(0,0,1)
        self.prob.mazeBelief.putVerticalWall(5,8,1)
        self.prob.mazeBelief.putVerticalWall(5,5,2)
        self.prob.mazeBelief.putVerticalWall(8,8,2)

        self.prob.mazeBelief.putHorizontalWall(4,7,0)
        self.prob.mazeBelief.putHorizontalWall(7,7,1)
        self.prob.mazeBelief.putHorizontalWall(3,5,2)
        self.prob.mazeBelief.putHorizontalWall(3,5,3)
        self.prob.mazeBelief.putHorizontalWall(7,7,3)

        self.prob.mazeBelief.putVerticalWall(6,7,4)
        self.prob.mazeBelief.putVerticalWall(5,6,5)
        self.prob.mazeBelief.putVerticalWall(5,7,7)

        # Posiciona fisicamente o agente no estado inicial
        initial = self.positionSensor()
        self.prob.defInitialState(initial.row, initial.col)
        self.cost = 0
        # Define o estado atual do agente = estado inicial
        self.currentState = self.prob.initialState
        # @TODO T_AAFP - defina estado objetivo
        # Define o estado objetivo
        # self.prob.defGoalState(?, ?)
        self.prob.defGoalState(2,8)
        # o metodo abaixo serve apenas para a view desenhar a pos objetivo
        # self.model.setGoalPos(2,8)
        self.model.setGoalPos(2,8)
        # Plano de busca - inicialmente vazio (equivale a solucao)
        self.plan = None


    def printPlan(self):
        """Apresenta o plano de busca."""
        print("--- PLANO ---")
        # @TODO: Implementação do aluno
        for plannedAction in self.plan:
            print("{} > ".format(action[plannedAction]),end='')
        print("FIM\n\n")

    def deliberate(self):
        # Primeira chamada, realiza busca para elaborar um plano
        # @TODO T_AAFP: Implementação do aluno
        if self.counter == -1:
            # @TODO T_AAFP: dar um plano fixo ao agente (preh-programado) - ver cardinal.py
            # @TODO T_AAFP: plano = solucao: contem acoes que levam o agente ateh o estado objetivo
            self.plan = [0,0,0,1,2,2,2,2,1,1]

            if self.plan != None:
                self.printPlan()
            else:
                print("SOLUÇÃO NÃO ENCONTRADA")
                return -1

        # Nas demais chamadas, executa o plano já calculado
        self.counter += 1

        # @TODO T_AAFP - testar se atingiu o estado objetivo ou se chegou ao final do plano sem alcancar o objetivo
        if(self.positionSensor() == self.prob.goalState):
            #colocar print final aqui
            print("*************** ultimo ciclo ***********************")
            print("estado atual:" + str(self.positionSensor()))
            print("açoes possiveis:")
            print("ct = "+ str(self.counter) +" de "+str(len(self.plan)))
            print("custo ate o momento (com a acao escolhida):"+str(self.cost))
            print("Objetivo conquistado!!!")
            print("****************************************************\n")
            return -1
        elif(self.counter == len(self.plan)):
                #colocar um print aqui depois
            print("*************** ultimo ciclo ***********************")
            print("estado atual:" + str(self.positionSensor()))
            print("açoes possiveis:")
            print("ct = "+ str(self.counter) +" de "+str(len(self.plan)))
            print("custo ate o momento (com a acao escolhida):"+str(self.cost))
            print("Objetivo nao conquistado!!")
            print("****************************************************\n")
            return -1


        currentAction = self.plan[self.counter]

        # @TODO T_AAFP - fazer prints solicitados
        #*************** inicio do ciclo ***********************
        #estado atual: (3,6)
        #açoes possiveis: {N NE SE S SO }
        #ct = 10 de 11. Ação escolhida=NE
        #custo ate o momento (com a acao escolhida): 11.5
        #****************************************************
        print("*************** inicio do ciclo ***********************")
        print("estado atual:" + str(self.positionSensor()))
        print("açoes possiveis:")
        print("ct = "+ str(self.counter) +" de "+str(len(self.plan))+  ". Ação escolhida=" +action[currentAction])
        print("custo ate o momento (com a acao escolhida):" + str(self.cost))
        print("****************************************************\n")
        # @TODO T_AAFP - o agente deve executar a acao e atualizar seu estado atual

        self.currentState = self.positionSensor()
        self.executeGo(currentAction)
        self.cost += self.prob.getActionCost(currentAction)
        
        return 1

    def executeGo(self, direction):
        """Atuador: solicita ao agente física para executar a ação.
        @param direction: Direção da ação do agente
        @return 1 caso movimentação tenha sido executada corretamente."""
        self.model.go(direction)
        return 1

    def positionSensor(self):
        """Simula um sensor que realiza a leitura do posição atual no ambiente e traduz para uma instância da classe Estado.
        @return estado que representa a posição atual do agente no labirinto."""
        pos = self.model.agentPos
        return State(pos[0],pos[1])
