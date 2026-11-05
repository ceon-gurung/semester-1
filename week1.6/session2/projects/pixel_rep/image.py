# Week 1.6, Session 2

"""
Classes for working with images.
"""

import copy


class ImageError(Exception):
    """
    Exception for problems that may occur when creating Image objects.
    """


class Image:
    """
    A greyscale image.
    """

    @classmethod
    def create(cls, width, height, value=0, maximum=255):
        """
        Creates an Image with the given dimensions.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        image = Image()
        image.create_pixels(width, height, value, maximum)
        return image

    @classmethod
    def read(cls, filename):
        print(("1 " * 20) + str(imagea.pixels))
        """
        Creates an Image from data in the specified PGM file.
        """
        image = Image()
        image = image.create(24, 7)
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """
        Creates a new array of pixels, replacing any existing image data.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        if width < 1:
            raise ImageError("width cannot be < 1")
        if height < 1:
            raise ImageError("height cannot be < 1")

        self.width = width
        self.height = height
        self.max_value = maximum
        self.pixels = [[value] * width] * height

    def read_pgm(self, filename):
        print(("2 " * 20) + str(imagea.pixels))
        """
        Reads data from the specified PGM image file into this Image.

        Any existing image data will be replaced.
        """
        with open(filename) as imgfile:
            self._parse_magic_number(imgfile)
            self._parse_dimensions(imgfile)
            self._parse_max_value(imgfile)
            self._parse_pixels(imgfile)

    def _parse_magic_number(self, imgfile):
        line = imgfile.readline().strip()
        if line != "P2":
            raise ImageError("unrecognized magic number")

    def _parse_dimensions(self, imgfile):
        line = imgfile.readline().strip()
        if line.startswith("#"):
            # Ignore comment and read another line
            line = imgfile.readline().strip()
        parts = line.split()
        self.width = int(parts[0])
        self.height = int(parts[1])

    def _parse_max_value(self, imgfile):
        line = imgfile.readline().strip()
        self.max_value = int(line)

    def _parse_pixels(self, imgfile):
        print(("3 " * 20) + str(imagea.pixels))
        dimens = [0, 0] # width, height
        contents = imgfile.readlines()
        for row in contents: # iterates through each row, or each list in imgfile.read()
            print("row: " + str(row))
            #print("row.split(): " + str(row.split()))
            dimens[0] += 1 # width
            dimens[1] = len(row.split()) # height
            self.pixels += [int(columnValue) for columnValue in row.split()] # each pixel is put into its own list index

        if dimens[0] * dimens[1] != self.width * self.height:
            print("dimens[0]: " + str(dimens[0]))
            print("dimens[1]: " + str(dimens[1]))
            print("self.width: " + str(self.width))
            print("self.height: " + str(self.height))
            raise ImageError("number of pixels doesn't match image dimensions")

        for row in imgfile.read():
            if any(p < 0 or p > self.max_value for p in row):
                raise ImageError(f"pixel value outside allowed range (0 to {self.max_value})")

    def __getitem__(self, index):
        """
        Returns pixel value at the specified linear index.
        """
        return self.pixels[index]

    def __setitem__(self, index, value):
        """
        Sets pixel at the specified linear index to the specified value.
        """
        self.pixels[index] = value

    def get(self, row, col):
        """
        Returns pixel value at the specified row & column coordinates.
        """
        index = row * self.width + col
        return self.pixels[index]

    def set(self, row, col, value):
        """
        Sets pixel at the specified row & column coordinates to the given value.
        """
        index = row * self.width + col
        self.pixels[index] = value

    def copy(self):
        """
        Returns a new Image that is a copy of this Image.
        """
        return copy.deepcopy(self)

    def write_pgm(self, filename):
        """
        Writes this Image to the specified PGM file.
        """
        with open(filename, "wt") as imgfile:
            self._write_header(imgfile)
            self._write_pixels(imgfile)

    def _write_header(self, imgfile):
        print("P2", file=imgfile)
        print(self.width, self.height, file=imgfile)
        print(self.max_value, file=imgfile)

    def _write_pixels(self, imgfile):
        for row in range(self.height): # using row, increments through the height
            start = row * self.width # current row number * total number of columns
            for value in self.pixels[start:start + self.width]: # iterates through an image's pixels 
                print(f"{value:4d}", end="", file=imgfile)
            print(file=imgfile)

imagea = Image()
imagea = imagea.create(24, 7)

print(("0 " * 20) + str(imagea.pixels))
imagea = imagea.read("/workspaces/semester-1/week1.6/session2/images/feep.pgm")

with open("/workspaces/semester-1/week1.6/session2/projects/pixel_rep/test.txt", "x") as f:
    for line in imagea:
        f.writelines(str(line) + "\n")