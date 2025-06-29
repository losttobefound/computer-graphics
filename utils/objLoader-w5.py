class objLoader:

    # Initialise variables for this class
    def __init__(self, path):
        self.path = path
        self.vertices = []
        self.faceVertexIndices = []
        self.__lines = []

        # Call the "read" function
        self.__read()

    def __read(self):

        # Open the file
        with open(self.path, "r") as f:

            # Go through each line in the file
            for line in f.readlines():

                # Add each line to list of lines, but remove leading and trailing
                # whitespace first:
                self.__lines.append(line.strip())

        # Go through each string in the list of lines
        for line in self.__lines:

            # If the line is a vertex position, call
            # the parse function
            if line.startswith("v "):
                self.__parse_v(line)

            # If line describes a face, parse with __parse_f
            if line.startswith("f "):
                self.__parse_f(line)

    def __parse_v(self, line):
        # Split the line into a list of strings
        vs = line.split(" ")

        # Remove the "v" at the beginning of the list
        vs.pop(0)

        # Convert the list of strings into a list of floats
        vf = [float(i) for i in vs]

        # Add each element of the list to the list of vertices
        self.vertices.extend(vf)

    def __parse_f(self, line):
        fs = line.split(" ") # "fs" because face data is stored as string in this variable

        # Remove first item in the list ("f")
        fs.pop(0)

        # Check the length. If not 3, mesh is not valid. Needs
        # to be triangulated
        if len(fs) != 3:
            raise ValueError("Mesh is not triangulated.")

        # fs looks like this:
        # ["v/vt/vn", "v/vt/vn",...]
        # Split each element by "/" so we get
        # [[v,vt,vn],[...],...]
        fsSplit = [el.split("/") for el in fs]

        for el in fsSplit:
            # Convert from string to integer
            eli = [int(i) for i in el]
            # ignore vt and vn, only store v (the first one)
            self.faceVertexIndices.append(eli[0])