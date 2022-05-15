class Player(Drawable):

    COLOR_LIST = [
        (37, 7, 255),
        (35, 183, 253),
        (48, 254, 241),
        (19, 79, 251),
        (255, 7, 230),
        (255, 7, 23),
        (6, 254, 13)]

    FONT_COLOR = (50, 50, 50)

    def __init__(self, surface, camera, name=""):
        super().__init__(surface, camera)
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.mass = 20
        self.speed = 4
        self.color = col = random.choice(Player.COLOR_LIST)
        self.outlineColor = (
            int(col[0] - col[0] / 3),
            int(col[1] - col[1] / 3),
            int(col[2] - col[2] / 3))
        if name:
            self.name = name
        else:
            self.name = "Anonymous"
        self.pieces = []

    def collisionDetection(self, edibles):

        for edible in edibles:
            if (getDistance((edible.x, edible.y), (self.x, self.y)) <= self.mass / 2):
                self.mass += 0.5
                edibles.remove(edible)

    def move(self):


        dX, dY = pygame.mouse.get_pos()
        # Find the angle from the center of the screen to the mouse in radians [-Pi, Pi]
        rotation = math.atan2(dY - float(SCREEN_HEIGHT) / 2, dX - float(SCREEN_WIDTH) / 2)
        # Convert radians to degrees [-180, 180]
        rotation *= 180 / math.pi
        # Normalize to [-1, 1]
        # First project the point from unit circle to X-axis
        # Then map resulting interval to [-1, 1]
        normalized = (90 - math.fabs(rotation)) / 90
        vx = self.speed * normalized
        vy = 0
        if rotation < 0:
            vy = -self.speed + math.fabs(vx)
        else:
            vy = self.speed - math.fabs(vx)
        tmpX = self.x + vx
        tmpY = self.y + vy
        self.x = tmpX
        self.y = tmpY

    def feed(self):

        pass

    def split(self):

        pass

    def draw(self):

        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        center = (int(self.x * zoom + x), int(self.y * zoom + y))

        # Draw the ouline of the player as a darker, bigger circle
        pygame.draw.circle(self.surface, self.outlineColor, center, int((self.mass / 2 + 3) * zoom))
        # Draw the actual player as a circle
        pygame.draw.circle(self.surface, self.color, center, int(self.mass / 2 * zoom))
        # Draw player's name
        fw, fh = font.size(self.name)
        drawText(self.name, (self.x * zoom + x - int(fw / 2), self.y * zoom + y - int(fh / 2)),
                 Player.FONT_COLOR)

    def draw(self):
        w, h = font.size("Score: " + str(int(blob.mass * 2)) + " ")
        MAIN_SURFACE.blit(pygame.transform.scale(SCOREBOARD_SURFACE, (w, h)),
                          (8, SCREEN_HEIGHT - 30))
        MAIN_SURFACE.blit(LEADERBOARD_SURFACE, (SCREEN_WIDTH - 160, 15))
        drawText("Score: " + str(int(blob.mass * 2)), (10, SCREEN_HEIGHT - 30))
        MAIN_SURFACE.blit(big_font.render("Leaderboard", 0, (255, 255, 255)),
                          (SCREEN_WIDTH - 157, 20))
        drawText("1. G #1", (SCREEN_WIDTH - 157, 20 + 25))
        drawText("2. G #2", (SCREEN_WIDTH - 157, 20 + 25 * 2))
        drawText("3. ISIS", (SCREEN_WIDTH - 157, 20 + 25 * 3))
        drawText("4. ur mom", (SCREEN_WIDTH - 157, 20 + 25 * 4))
        drawText("5. w = pro team", (SCREEN_WIDTH - 157, 20 + 25 * 5))
        drawText("6. jumbo", (SCREEN_WIDTH - 157, 20 + 25 * 6))
        drawText("7. [voz]plz team", (SCREEN_WIDTH - 157, 20 + 25 * 7))
        drawText("8. G #3", (SCREEN_WIDTH - 157, 20 + 25 * 8))
        drawText("9. doge", (SCREEN_WIDTH - 157, 20 + 25 * 9))
        if (blob.mass <= 500):
            drawText("10. G #4", (SCREEN_WIDTH - 157, 20 + 25 * 10))
        else:
            drawText("10. adrien", (SCREEN_WIDTH - 157, 20 + 25 * 10), (210, 0, 0))