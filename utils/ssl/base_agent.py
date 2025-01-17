from rsoccer_gym.Entities import Robot
from utils.Point import Point

class BaseAgent:
    """Abstract Agent."""

    #informações do robo(perguntar sobre dict)
    def __init__(self, id=0, yellow=False):
        self.id = id
        self.robot = Robot()
        self.pos = Point(0, 0)
        self.vel = Point(0, 0)
        self.body_angle = float(0)
        self.targets = []
        self.yellow = yellow
        self.opponents = dict()
        self.teammates = dict()

        self.next_vel = Point(0, 0)
        self.angle_vel = float(0)

    #informações do próprio robo sobre a partida
    def step(self, self_robot : Robot, 
             opponents: dict[int, Robot] = dict(), 
             teammates: dict[int, Robot] = dict(), 
             targets: list[Point] = [], 
            #keep targets parece ser interessante pro projeto
             keep_targets=False) -> Robot:

        #posição e velocidade atual
        self.reset()
        self.pos = Point(self_robot.x, self_robot.y)
        self.vel = Point(self_robot.v_x, self_robot.v_y)
        self.body_angle = self_robot.theta

        #função que define se há alvo, se tiver ele vai seco ou tem esse keep targets q vou tentar entender melhor
        if len(targets) > 0:
            self.targets = targets.copy()
        elif len(self.targets) == 0 or not keep_targets:
            self.targets = []
            
        #define para o robo quem é oponente e quem é do time
        self.robot = self_robot
        self.opponents = opponents.copy()
        self.teammates = teammates.copy()

        #(tentar entender isso aqui)
        self.decision()
        self.post_decision()

        #retorna essas informações pro robo
        return Robot( id=self.id, yellow=self.yellow,
                      v_x=self.next_vel.x, v_y=self.next_vel.y, v_theta=self.angle_vel)

    #parar o robo
    def reset(self):
        self.next_vel = Point(0, 0)
        self.angle_vel = 0

    #??
    def decision(self):
        raise NotImplementedError()
    
    #??
    def post_decision(self):
        raise NotImplementedError()
    
    #mudança de velocidade?
    def set_vel(self, vel: Point):
        self.next_vel = vel
    
    #mudança de velocidade angular?
    def set_angle_vel(self, angle_vel: float):
        self.angle_vel = angle_vel
