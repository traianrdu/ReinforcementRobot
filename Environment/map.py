from Environment.cart import Cart, Vector2, pygame
from Environment.object_static import StaticObj
from Environment.object_dynamic import DynamicObj


class Map:
    # define the colors
    BLACK = (25, 25, 25)
    WHITE = (255, 255, 255)
    RED = (255, 80, 80)
    BLUE = (80, 80, 255)

    def __init__(self, width: int, length: int, start_point: Vector2):
        """Initializes the map"""
        pygame.init()  # starts the environment
        self.width = width  # width of the screen
        self.length = length  # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.length))  # set the screen dimensions
        self.screen.fill(self.WHITE)    # set the background as white
        #self.road = Road(self.screen, self.WHITE)
        self.static_object = StaticObj(80, 40, Vector2(300, 300), self.BLACK, self.screen)
        self.dynamic_object = DynamicObj(20, 60, Vector2(100, 100), self.BLUE, self.screen)
        self.cart = Cart(20, 20, Vector2(400, 400), self.RED, self.screen)  # initializes the car class
        self.render()  # render the environment

        self.running = False  # is the game running or not

    def render(self):
        """Renders the environment"""
        pygame.display.set_caption('RiCart')  # title of the simulator
        #self.road.render()  # render the road
        self.static_object.render()  # render static object
        self.cart.render()  # render the car
        self.dynamic_object.render()  # render dynamic object
        pygame.display.flip()  # shows on screen

    def handle_events(self):
        """Handle the press key events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

    def run(self):
        """Starts the environment loop"""
        self.running = True
        while self.running:
            self.handle_events()  # handles the events of the game

        pygame.quit()
