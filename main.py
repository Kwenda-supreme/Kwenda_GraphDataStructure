class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            else:
                self.graph_dict[start] = [end]

        # Printing all the routes initialized in routes
        print("This is A program to calculate shortest route between landmarks")
        landmarks = ["1. Ma Tank Petroda", "2. Institute for Youth", "3. Shoprite", "4. Lilongwe Sanctuary",
                     "5. Area 18 Interchange", "6. Area 25", "7. Kanengo"]
        print("The landmarks of Lilongwe city are: ")
        for i in landmarks:
            print(i)

    # calculating shortest path
    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict and end not in self.graph_dict:
            return print("Invalid Selection, Please Select From the Above list")

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                short = self.get_shortest_path(node, end, path)
                if short:
                    if shortest_path is None or len(short) < len(shortest_path):
                        shortest_path = short

        return shortest_path


# Defining routes
if __name__ == '__main__':
    routes = [
        ("bunda turnoff", "likuni rb"), ("likuni rb", "bunda turnoff"),
        ("bunda turnoff", "ma tank petroda"), ("ma tank petroda", "bunda turnoff"),
        ("ma tank petroda", "institute for youth"), ("institute for youth", "ma tank petroda"),
        ("institute for youth", "lilongwe sanctuary"), ("lilongwe sanctuary", "institute for youth"),
        ("ma tank petroda", "town hall rb"), ("town hall rb", "ma tank petroda"),
        ("likuni rb", "town hall rb"), ("town hall rb", "likuni rb"),
        ("likuni rb", "mchinji rb"), ("mchinji rb", "likuni rb"),
        ("town hall rb", "shoprite"), ("shoprite", "town hall rb"),
        ("shoprite", "crossroads rb"), ("crossroads rb", "shoprite"),
        ("mchinji rb", "crossRoads rb"), ("crossRoads rb", "mchinji rb"),
        ("crossRoads rb", "chilambula rb"), ("chilambula rb", "crossroads rb"),
        ("chilambula rb", "kch rb"), ("kch rb", "chilambula rb"),
        ("kch rb", "shoprite"), ("shoprite", "kch rb"),
        ("kch rb", "lilongwe sanctuary"), ("lilongwe sanctuary", "kch rb"),
        ("lilongwe sanctuary", "parliament rb"), ("parliament rb", "lilongwe sanctuary"),
        ("chilambula rb", "bwandilo tj"), ("bwandilo tj", "chilambula rb"),
        ("crossroads rb", "bwandilo tj"), ("bwandilo tj", "crossroads rb"),
        ("mchinji rb", "bingu stadium rb"), ("bingu stadium rb", "mchinji rb"),
        ("bwandilo tj", "area 18 interchange"), ("area 18 interchange", "bwandilo tj"),
        ("area 18 interchange", "parliament rb"), ("parliament rb", "area 18 interchange"),
        ("area 18 interchange", "bingu stadium rb"), ("bingu stadium rb", "area 18 interchange"),
        ("bingu stadium rb", "area 25"), ("area 25", "bingu stadium rb"),
        ("area 18 interchange", "kanengo"), ("kanengo", "area 18 interchange"),
        ("area 25", "bingu stadium rb"), ("bingu stadium rb", "area 25"),
        ("area 25", "kanengo"), ("kanengo", "area 25"),

    ]

    route_graph = Graph(routes)

    # Prompt user to enter point of origin
    origin = input("Please select from the List Above and enter Starting Point: ")
    start = origin.lower()

    # Prompt user to enter destination
    destination = input("Please select from the list above and enter Destination: ")
    end = destination.lower()

    # shortest path
    print(f"The Quickest route between", start, " and", end, " is : ", route_graph.get_shortest_path(start, end))
