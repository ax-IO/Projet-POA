# class AgentCat(pai.gameobject.GameObject):

#     def __init__(self, pos = (0, 0)):
#         # First we create the image by filling a surface with blue color
#         img = pygame.Surface( (10, 15) ).convert()
#         img.fill(BLUE)
#         # Call GameObject init with appropiate values
#         super(AgentCat, self).__init__(
#             img_surf = img,
#             pos = pos,
#             max_speed = 15,
#             max_accel = 40,
#             max_rotation = 40,
#             max_angular_accel = 30
#         )