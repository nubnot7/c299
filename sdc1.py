from controller import Robot

bot = Robot()

timestep = 64

# getting devices
# get the camera device

cam = bot.getDevice('camera')
left_wheel = bot.getDevice('left_front_wheel')
right_wheel = bot.getDevice('right_front_wheel')
l_steer = bot.getDevice('left_steer')
r_steer = bot.getDevice('right_steer')

# enable the camera
cam.enable(timestep)
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
l_steer.setPosition(0)
r_steer.setPosition(0)
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)

while bot.step(timestep) != -1:

    img = cam.getImage()
    image_width = cam.getWidth()
    image_height = cam.getHeight()
    
    x_yellow = []
    for x in range(0, image_height):
        for y in range(0, image_height):
            red_val = cam.imageGetRed(img, image_width, x, y)
            green_val = cam.imageGetGreen(img, image_width, x, y)
            blue_val = cam.imageGetBlue(img, image_width, x, y)
            if red_val > 190 and green_val > 180 and blue_val > 90:
                x_yellow.append(x)
            
        if x_yellow: 
            x_total = 0 
            for x in x_yellow:
                x_total = x_total + x
            x_average = x_total / len(x_yellow)
            x_center = image_width / 2
            
        if x_average < x_center:
            l_steer.setPosition(-0.1)
            r_steer.setPosition(-0.1)
        elif x_average > x_center:
            l_steer.setPosition(0.1)
            r_steer.setPosition(0.1)
            
        left_wheel.setVelocity(10)
        right_wheel.setVelocity(10)