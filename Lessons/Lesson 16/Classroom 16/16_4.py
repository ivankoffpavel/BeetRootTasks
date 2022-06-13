class CMYK:
    def __init__(self, c, m, y, k):
        self.cmyk = [c, m, y, k]

        white = 1 - float(self.cmyk[3])
        self.red = round(255 * white * (1 - float(self.cmyk[0])))
        self.green = round(255 * white * (1 - float(self.cmyk[1])))
        self.blue = round(255 * white * (1 - float(self.cmyk[2])))

    def __repr__(self):
        return f'R - {str(self.red)}, G - {str(self.green)}, B - {str(self.blue)}'


color = CMYK(0.1, 0.1, 0.1, 0.1)
print(color)