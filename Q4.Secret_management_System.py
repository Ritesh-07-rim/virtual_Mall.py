class Agent:
    def __init__(self,name, agent_id, __salary):
        self.name = name
        self.agent_id = agent_id
        self.__salary = __salary

    def show_salary(self):
        print("Salary :",self.__salary)    


class FieldAgent(Agent):
    def mission(self):
        print("Agent - Name :",self.name)
        print("Agent - id :",self.agent_id)
        self.show_salary()
        print("complting field mission")
        print()
               

class CyberAgent(Agent):
    def mission(self):
        print("Agent - Name :",self.name)
        print("Agent - id :",self.agent_id)
        self.show_salary()
        print("Hacking into the system")


agents =[
    FieldAgent("Rahul","BC-17",2500000),
    CyberAgent("Deva","MC-09",5600000)
]

for agent in agents:
    agent.mission()
                         