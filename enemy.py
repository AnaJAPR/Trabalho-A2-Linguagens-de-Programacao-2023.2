import pygame
import math
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self._speed = 1
        self._health = 1
        self._xp = 1

        self.__waypoints = waypoints
        self.__target_wp = 1

        self.__position = Vector2(self.__waypoints[0])
        self.__angle = 0
        self._original_image = image
        self._image= pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self._image.get_rect()
        self.rect.center = self.__position

    def update(self):
        self.move()
        self.rotate()

    # Method to make the enemy move
    def move(self):
        # Defining the target and the movement
        if self.__target_wp < len(self.__waypoints):
            self.__target = Vector2(self.__waypoints[self.__target_wp])
            self.__movement = self.__target - self.__position
        # If there are no more waypoints to go, the enemy disappears
        else:
            self.kill()

        distance = self.__movement.length()
        # If the distance to the next waypoint is greater than the enemy's speed, it will move at its natural speed
        if distance >= self._speed:
            self.__position += self.__movement.normalize() * self._speed
        else:
            # While the distance is less than the enemy speed, the movement speed is equal to the distance
            if distance != 0:
                self.__position += self.__movement.normalize() * distance
            # Once the distance gets to 0, the next waypoint becomes into the new target
            self.__target_wp += 1

        self.rect.center = self.__position
    
    def rotate(self):
        #calculate distance to next waypoint
        dist = self.__target - self.__position
        #use distance to calculate angle
        self.__angle = math.degrees(math.atan2(-dist[1], dist[0]))
        #rotate image and update rectangle
        self.image= pygame.transform.rotate(self._original_image, self.__angle)
        self.rect = self._image.get_rect()
        self.rect.center = self.__position

# class Enemy_1(Enemy):
#     def __init__(self, waypoints, image):
#         super().__init__(waypoints, image)

        
