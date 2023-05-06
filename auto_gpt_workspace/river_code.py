class River:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def flow(self):
        '''Returns a string that describes the flow of the river.'''
        return f'The {self.name} river is flowing.'

    def validate_input(self):
        '''Validates that the length and width of the river are positive numbers.'''
        if self.length <= 0 or self.width <= 0:
            raise ValueError('Length and width must be positive numbers.')