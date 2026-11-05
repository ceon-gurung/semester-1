class Image:
    def initialiseImage(width, height, value=0, max=255):
        newImage = [["P2"], [str(width) + " " + str(height)], [max], [[0] * width] * height]
        return newImage

    def copyImage(self, imageFileName):
        with open(imageFileName, 'r') as f:
            contents = f.readlines()

            if not contents[0] == "P2":
                raise ValueError("a")

            self.

imagea = Image.initialiseImage(24, 7)

Image.copyImage("/workspaces/semester-1/week1.6/session2/images/feep.pgm")