class CellList(Drawable):

    def __init__(self, surface, camera, numOfCells):
        super().__init__(surface, camera)
        self.count = numOfCells
        self.list = []
        for i in range(self.count): self.list.append(Cell(self.surface, self.camera))

    def draw(self):
        for cell in self.list:
            cell.draw()

cam = Camera()

grid = Grid(MAIN_SURFACE, cam)
cells = CellList(MAIN_SURFACE, cam, 2000)
blob = Player(MAIN_SURFACE, cam, "GeoVas")
hud = HUD(MAIN_SURFACE, cam)

painter = Painter()
painter.add(grid)
painter.add(cells)
painter.add(blob)
painter.add(hud)

while (True):

    clock.tick(70)

    for e in pygame.event.get():
        if (e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if (e.key == pygame.K_SPACE):
                del (cam)
                blob.split()
            if (e.key == pygame.K_w):
                blob.feed()
        if (e.type == pygame.QUIT):
            pygame.quit()
            quit()

    blob.move()
    blob.collisionDetection(cells.list)
    cam.update(blob)
    MAIN_SURFACE.fill((242, 251, 255))

    painter.paint()

    pygame.display.flip()

class Cell(Drawable):  # Semantically, this is a parent class of player

    CELL_COLORS = [
        (80, 252, 54),
        (36, 244, 255),
        (243, 31, 46),
        (4, 39, 243),
        (254, 6, 178),
        (255, 211, 7),
        (216, 6, 254),
        (145, 255, 7),
        (7, 255, 182),
        (255, 6, 86),
        (147, 7, 255)]

    def __init__(self, surface, camera):
        super().__init__(surface, camera)
        self.x = random.randint(20, 1980)
        self.y = random.randint(20, 1980)
        self.mass = 7
        self.color = random.choice(Cell.CELL_COLORS)

    def draw(self):

        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        center = (int(self.x * zoom + x), int(self.y * zoom + y))
        pygame.draw.circle(self.surface, self.color, center, int(self.mass * zoom))