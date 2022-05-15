class Painter:


    def __init__(self):
        self.paintings = []

    def add(self, drawable):
        self.paintings.append(drawable)

    def paint(self):
        for drawing in self.paintings:
            drawing.draw()


class Camera:


    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.zoom = 0.5

    def centre(self, blobOrPos):

        if isinstance(blobOrPos, Player):
            x, y = blobOrPos.x, blobOrPos.y
            self.x = (x - (x * self.zoom)) - x + (SCREEN_WIDTH / 2)
            self.y = (y - (y * self.zoom)) - y + (SCREEN_HEIGHT / 2)
        elif type(blobOrPos) == tuple:
            self.x, self.y = blobOrPos

    def update(self, target):
        self.zoom = 100 / (target.mass) + 0.3
        self.centre(blob)


class Drawable:


    def __init__(self, surface, camera):
        self.surface = surface
        self.camera = camera

    def draw(self):
        pass


class Grid(Drawable):


    def __init__(self, surface, camera):
        super().__init__(surface, camera)
        self.color = (230, 240, 240)

    def draw(self):
        # A grid is a set of horizontal and prependicular lines
        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        for i in range(0, 2001, 25):
            pygame.draw.line(self.surface, self.color, (x, i * zoom + y), (2001 * zoom + x, i * zoom + y), 3)
            pygame.draw.line(self.surface, self.color, (i * zoom + x, y), (i * zoom + x, 2001 * zoom + y), 3)