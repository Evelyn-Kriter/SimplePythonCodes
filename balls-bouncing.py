#Evey Kriter/CSCI0101/12.1.2019/Lab 10

import turtle  # Using Turtle and Screen classes
import random  # Using randint

class Ball:
    """
    A class representing a ball on the screen
    
    Attributes
    ----------
    turtle : Turtle 
        A Turtle type object from the module turtle
    x : float
        The x coordinate of the ball
    y : float
        The y coordinate of the ball
    radius : float
        The radius of the ball
    velocity : list
        The x and y components of the velocity of the ball
    color : string
        The color of the ball
    exploding : bool
            Is the ball exploding?
        done : bool
            Is the ball done exploding?
    
    Methods
    -------
    update()
        Update the ball location and exploding status each time it is called
    collide(other)
        Check for collision with another ball
    swap_velocity(other)
        Bounce this ball off another ball
    draw()
        Draw the ball on the screen
    """
    
    def __init__(self, t, x , y , radius, vx, vy, color, exploding, done):
        """
        Parameters
        ----------
        t : turtle
            A turtle type object from the module turtle
        radius : float
            The radius of the ball
        x : float
            The x coordinate of the ball
        y : float
            The y coordinate of the ball
        vx : float
            The x component of the ball velocity
        vy : float
            The y component of the ball velocity
        velocity : list
            The x and y components of the velocity of the ball
        color : string
            The color of the ball
        exploding : bool
            Is the ball exploding?
        done : bool
            Is the ball done exploding?
        """
        # Store the parameters in the new object atributes
        self.turtle = t
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = [vx, vy]
        self.color = color
        self.exploding = exploding
        self.done = done
        
        
    def update(self):
        """
        Update the ball status:
        - Check if the ball should bounce off the window edges
        - Update position using the velocity
        """
        # Acquire the screen instance from the turtle
        screen = turtle.Screen()
        
        # Store current screen properties
        width = screen.window_width() 
        height = screen.window_height()
        
        # Check for boundaries
        if (self.x - self.radius <= -width//2) or (self.x + self.radius >= width//2):
            self.velocity[0] *= -1
        if (self.y - self.radius <= -height//2) or (self.y + self.radius >= height//2):
            self.velocity[1] *= -1
        
        #Check for explosions
        if self.exploding == True:
            self.velocity == [0,0]
            if self.radius < 40:
                self.radius = self.radius + 1
                self.done = False
            elif self.radius == 40:
                self.done = True
        
        
        # Update position with velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
    def collide(self, other):
        """
        Check if this ball is colliding with another ball
        
        Parameters
        ----------
        other : ball
            Another ball to be checked for collision
        """
        
        # Evaluate the difference in coordinates between this and other
        dx = self.x - other.x
        dy = self.y - other.y
        
        # Check if the balls collided
        return (self.radius + other.radius) * (self.radius + other.radius) >= (dx * dx + dy * dy)
    
    def swap_velocity(self, other):
        """
        Bounce this ball off another ball
        
        Parameters
        ----------
        other : ball
            Another ball to bounce off
        """
        # Swap the velocities to simulate bouncing
        old_velocity = self.velocity
        self.velocity = other.velocity
        other.velocity = old_velocity
        
    def draw(self):
        """
        Draw the ball on the screen
        """
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.dot(self.radius * 2, self.color)
        
        

class Game:
    """
    A class implementing the multiple ball scene
    
    Attributes
    ----------
    screen : Screen
        A Screen type object from the module turtle
    turtle : Turtle
        A Turtle type object from the module turtle
        
    
    Methods
    -------
    initialize_objs()
        Create the gamefield by adding the balls
    run()
        Determines the game dynamic frame by frame (one frame for each call)
    done()
        Exit the program
    """
    def __init__(self):
        # Create a screen object (singleton) and set it up
        self.screen = turtle.Screen()
        self.screen.setup(0.5, 0.5)  # Use half with and half height of your current screen
        self.screen.tracer(False)
        self.screen.colormode(255)
        
        # Create an invisible turtle object
        self.turtle = turtle.Turtle(visible=False)
        
        # Initialize the scene
        self.initialize_objs()
    
        # Defines users' interactions we should listen for
        self.screen.onkey(self.done, 'r')  # Check if user pushed 'q'
        self.screen.onclick(self.add_bomb) # Check if the user added a bomb
        
        # As soon as the event loop is running, set up to call the self.run() method
        self.screen.ontimer(self.run, 0)
    
        # Tell the turtle screen to listen to the users' interactions
        self.screen.listen()
        
        # Start the event loop
        self.screen.mainloop()
        
    def initialize_objs(self):
        """
        Initializes the scene
        """
        # Defines the size of the game field       
        width = self.screen.window_width() - 20
        height = self.screen.window_height() - 20

        # Empty list to hold all the balls
        self.objects = []
        
        # Add balls to the game field with random location, velocity, and color        
        for _ in range(5):
            ball = Ball(self.turtle,
                        random.randint(-width//2, width//2),    # X-location 
                        random.randint(-height//2, height//2),  # Y-location
                        10,                                     # radius
                        random.randint(-3, 3),                  # velocity: x-component
                        random.randint(-3, 3),                  # velocity: y-component
                        (random.randint(0, 255),                # color: red
                         random.randint(0, 255),                # color: green
                         random.randint(0, 255)),               # color: blue
                        False,                                  # exploding: no
                        False)                                  # done: no
            self.objects.append(ball)
        
        
    def run(self):
        """
        Determines the game dynamic frame by frame (one frame for each call)
        """
        # Clear the screen
        self.turtle.clear()
        
        # Check the state of every ball
        for i in range(len(self.objects)):
            obj1 = self.objects[i]
            # Check interaction with every other ball
            for j in range(i+1, len(self.objects)):
                obj2 = self.objects[j]
                # If we collide with another ball, either bounce off each other or explode
                if obj1.collide(obj2):
                    if obj2.exploding == True or obj1.exploding == True:
                        obj1.velocity = [0,0]
                        obj1.exploding = True
                        obj2.velocity = [0,0] #this seems uneccessary but I had to do it to fix a bug
                        obj2.exploding = True #''
                    else:
                        obj1.swap_velocity(obj2)
                    
            # Update and draw current ball
            obj1.update()
            obj1.draw()
            
        # Update the overall screen
        self.screen.update()
        
        # This will keep track of all the exploding balls and give us a score in the end
        score = [self.objects[b].done for b in range(len(self.objects)) if self.objects[b].exploding == True]
        
        if len(score) == 0:
                self.screen.ontimer(self.run, 0)

        for x in range(len(score)):
            if score[x] == False:
                self.screen.ontimer(self.run, 0)
            else:
                turtle.color('black')
                style = ('Courier', 20, 'italic')
                turtle.penup()
                turtle.goto(-650,-400)
                turtle.pendown()
                turtle.write('Game over! You exploded ' + str(len(score) - 1) + '/' + str(len(self.objects)) + ' balls.', font=style)
                turtle.hideturtle() 
                    
    def add_bomb(self, x , y):
        alist = [n for n in range(len(self.objects)) if self.objects[n].exploding == True]
        if len(alist) == 0:
            bomb = Ball(self.turtle,
                        x,                                      # X-location 
                        y,                                      # Y-location
                        10,                                     # radius
                        0,                                      # velocity: x-component
                        0,                                      # velocity: y-component
                        (0,0,0),                                # color: black
                        True,                                   # exploding: yes
                        False)                                  # done: no                                
            self.objects.append(bomb)
        else:
            pass
        
    def done(self):
        """
        restart the program
        """
        self.screen.clear()
        game = Game()


# Draw the scene
game = Game()


