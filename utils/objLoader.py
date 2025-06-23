class objLoader:

    # Initialise variables for this class
    def __init__(self, path):
        self.path = path
        self.vertices = []
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

    def __parse_v(self, line):
        # Split the line into a list of strings
        vs = line.split(" ")

        # Remove the "v" at the beginning of the list
        vs.pop(0)

        # Convert the list of strings into a list of floats
        vf = [float(i) for i in vs]

        # Add each element of the list to the list of vertices
        self.vertices.extend(vf)
                
    # def __parse_v(self, line):
    #     # Sauber splitten (beliebige Leerzeichen)
    #     vs = line.strip().split()

    #     # Sicherstellen, dass mindestens 3 Werte vorhanden sind
    #     if len(vs) < 4:
    #         print(f"Warnung: Ungültiger Vertex-Eintrag übersprungen → {line}")
    #         return

    #     # "v" entfernen und Rest in float umwandeln
    #     try:
    #         vf = [float(i) for i in vs[1:4]]  # Nur die ersten drei Werte verwenden
    #         self.vertices.extend(vf)
    #     except ValueError as e:
    #         print(f"Fehler beim Parsen der Zeile '{line}': {e}")