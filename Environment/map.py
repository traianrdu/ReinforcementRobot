from Environment.cart import Cart, Vector2, pygame
from Environment.object_static import StaticObj
from Environment.object_dynamic import DynamicObj
from Environment.leader import Leader
from enum import Enum


class Direction(Enum):
    N = 1
    S = 2
    E = 3
    W = 4
    NE = 5
    NW = 6
    SE = 7
    SW = 8


class Map:
    # define the colors
    BLACK = (25, 25, 25)
    WHITE = (255, 255, 255)
    RED = (255, 80, 80)
    BLUE = (80, 80, 255)
    GREEN = (0, 255, 0)
    DIRECTIONS = ["N", "S", "E", "W", "NW", "NE", "SW", "SE"]
    STEPS = 100

    def __init__(self, width: int, length: int, start_point: Vector2):
        """Initializes the map"""
        pygame.init()  # starts the environment
        pygame.display.set_caption('RiCart')  # title of the simulator
        self.width = width  # width of the screen
        self.length = length  # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.length))  # set the screen dimensions
        self.screen.fill(self.WHITE)  # set the background as white
        self.direction = Direction.N
        # initializes the static obj
        self.static_object1 = StaticObj(140, 40, Vector2(40, 300), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object2 = StaticObj(140, 40, Vector2(40, 500), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object3 = StaticObj(140, 40, Vector2(40, 700), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object11 = StaticObj(260, 40, Vector2(260, 300), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object21 = StaticObj(260, 40, Vector2(260, 500), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object31 = StaticObj(260, 40, Vector2(260, 700), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object12 = StaticObj(260, 40, Vector2(580, 300), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object22 = StaticObj(260, 40, Vector2(580, 500), self.BLACK, self.screen, self.DIRECTIONS)
        self.static_object32 = StaticObj(260, 40, Vector2(580, 700), self.BLACK, self.screen, self.DIRECTIONS)
        # initializes the dynamic obj
        self.dynamic_object1 = DynamicObj(20, 80, Vector2(100, 100), self.BLUE, self.screen, self.DIRECTIONS)
        self.dynamic_object2 = DynamicObj(20, 30, Vector2(400, 100), self.BLUE, self.screen, self.DIRECTIONS)
        self.dynamic_object3 = DynamicObj(30, 30, Vector2(100, 600), self.BLUE, self.screen, self.DIRECTIONS)
        self.dynamic_object4 = DynamicObj(20, 60, Vector2(100, 800), self.BLUE, self.screen, self.DIRECTIONS)
        self.dynamic_object5 = DynamicObj(20, 10, Vector2(500, 600), self.BLUE, self.screen, self.DIRECTIONS)
        self.leader = Leader(20, 20, Vector2(500, 400), self.GREEN, self.screen,
                             self.DIRECTIONS)  # initializes the leader
        self.cart = Cart(20, 20, Vector2(400, 400), self.RED, self.screen, self.DIRECTIONS)  # initializes the cart
        self.all_sprites = pygame.sprite.Group([self.static_object1, self.dynamic_object1, self.dynamic_object2,
                                                self.dynamic_object3, self.dynamic_object4, self.dynamic_object5,
                                                self.static_object2, self.static_object3, self.static_object11,
                                                self.static_object21, self.static_object31, self.static_object12,
                                                self.static_object22, self.static_object32,
                                                self.leader, self.cart])
        self.cart.set_late_objects(self.object_list_without_current(self.cart))
        self.render()  # render the environment

        self.running = False  # is the game running or not

    def render(self):
        """Renders the environment on the first run"""
        self.screen.fill(self.WHITE)  # reset screen
        self.all_sprites.draw(self.screen)  # render all objects
        # self.static_object.render(self.screen)  # render static object
        # self.dynamic_object.render(self.screen)  # render dynamic object
        self.dynamic_object1.render()
        self.dynamic_object2.render()
        self.dynamic_object3.render()
        self.dynamic_object4.render()
        self.dynamic_object5.render()
        self.leader.render()  # render the car
        self.cart.render()  # render the car
        pygame.display.flip()  # shows on screen

    def reset(self):
        """Reset the map"""
        self.dynamic_object1.reset()
        self.dynamic_object2.reset()
        self.dynamic_object3.reset()
        self.dynamic_object4.reset()
        self.dynamic_object5.reset()
        self.leader.reset()
        self.cart.reset()
        self.render()

    def object_list_without_current(self, current_object):
        """Returns the object list without the current one"""
        all_obj = self.all_sprites.copy()  # list of objects
        if current_object in all_obj:
            all_obj.remove(current_object)
        return all_obj
