from Environment.cart import Cart, Vector2, pygame
from Environment.object_static import StaticObj
from Environment.object_dynamic import DynamicObj
from Environment.leader import Leader


class Map:
    # define the colors
    BLACK = (25, 25, 25)
    WHITE = (255, 255, 255)
    RED = (255, 80, 80)
    BLUE = (80, 80, 255)
    GREEN = (0, 255, 0)

    def __init__(self, width: int, length: int, start_point: Vector2):
        """Initializes the map"""
        pygame.init()  # starts the environment
        pygame.display.set_caption('RiCart')  # title of the simulator
        self.width = width  # width of the screen
        self.length = length  # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.length))  # set the screen dimensions
        self.screen.fill(self.WHITE)    # set the background as white
        # initializes the static obj
        self.static_object1 = StaticObj(140, 40, Vector2(40, 300), self.BLACK, self.screen)
        self.static_object2 = StaticObj(140, 40, Vector2(40, 500), self.BLACK, self.screen)
        self.static_object3 = StaticObj(140, 40, Vector2(40, 700), self.BLACK, self.screen)
        self.static_object11 = StaticObj(260, 40, Vector2(260, 300), self.BLACK, self.screen)
        self.static_object21 = StaticObj(260, 40, Vector2(260, 500), self.BLACK, self.screen)
        self.static_object31 = StaticObj(260, 40, Vector2(260, 700), self.BLACK, self.screen)
        self.static_object12 = StaticObj(260, 40, Vector2(580, 300), self.BLACK, self.screen)
        self.static_object22 = StaticObj(260, 40, Vector2(580, 500), self.BLACK, self.screen)
        self.static_object32 = StaticObj(260, 40, Vector2(580, 700), self.BLACK, self.screen)
        # initializes the dynamic obj
        self.dynamic_object = DynamicObj(20, 80, Vector2(100, 100), self.BLUE, self.screen)
        self.leader = Leader(20, 20, Vector2(500, 400), self.GREEN, self.screen)  # initializes the leader
        self.cart = Cart(20, 20, Vector2(400, 400), self.RED, self.screen)  # initializes the cart
        self.all_sprites = pygame.sprite.Group([self.static_object1, self.dynamic_object, self.leader, self.cart,
                                                self.static_object2, self.static_object3, self.static_object11,
                                                self.static_object21, self.static_object31, self.static_object12,
                                                self.static_object22, self.static_object32])
        self.objects = pygame.sprite.Group([self.static_object1, self.dynamic_object, self.cart, self.static_object2,
                                            self.static_object3, self.static_object11, self.static_object21,
                                            self.static_object31, self.static_object12, self.static_object22,
                                            self.static_object32])
        self.render()  # render the environment

        self.running = False  # is the game running or not

    def render(self):
        """Renders the environment on the first run"""
        self.screen.fill(self.WHITE)    # reset screen
        self.all_sprites.draw(self.screen)  # render all objects
        #self.static_object.render(self.screen)  # render static object
        #self.dynamic_object.render(self.screen)  # render dynamic object
        self.leader.render()  # render the car
        self.cart.render()  # render the car
        pygame.display.flip()  # shows on screen

    def handle_events(self):
        """Handle the press key events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

        keys = pygame.key.get_pressed()     # return pressed key

        self.leader.keyboard_move(keys, self.objects)
        self.render()   # render the simulation

    def run(self):
        """Starts the environment loop"""
        self.running = True
        while self.running:
            self.handle_events()  # handles the events of the game

        pygame.quit()
