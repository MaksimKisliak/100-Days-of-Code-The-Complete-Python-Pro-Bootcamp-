# First, we define a base class PixelaApi with some common properties and methods that all other classes will inherit from:
class PixelaApi:
    endpoint = "https://pixe.la/v1/users"

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.headers = {"X-USER-TOKEN": token}

    def make_request(self, url, method="GET", data=None):
        if method == "GET":
            response = requests.get(url=url, headers=self.headers)
        elif method == "POST":
            response = requests.post(url=url, json=data, headers=self.headers)
        elif method == "PUT":
            response = requests.put(url=url, json=data, headers=self.headers)
        elif method == "DELETE":
            response = requests.delete(url=url, headers=self.headers)
        else:
            raise ValueError("Invalid HTTP method")

        response.raise_for_status()
        return response.json()

# This class has an endpoint property, which is the base URL of the Pixela API. It also has an __init__ method that initializes the username, token, and headers properties with the given arguments.
# The make_request method is used to make HTTP requests to the API. It takes a URL, an HTTP method (defaulting to GET), and optional data as arguments, and returns the JSON response of the request.
# Next, we define a PixelaUser class that inherits from the PixelaApi class. This class represents a user in the Pixela API and has methods to create and delete a user:
class PixelaUser(PixelaApi):
    def create_user(self, agree_terms_of_service=True, not_minor=True):
        data = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes" if agree_terms_of_service else "no",
            "notMinor": "yes" if not_minor else "no",
        }
        url = f"{self.endpoint}"
        self.make_request(url, "POST", data)

    def delete_user(self):
        url = f"{self.endpoint}/{self.username}"
        self.make_request(url, "DELETE")

# The create_user method sends a POST request to the API with the user data, and the delete_user method sends a DELETE request to delete the user.
# The PixelaGraph class inherits from PixelaApi and has an additional graph_id attribute that represents the ID of the graph in the Pixela API. It also has a graph_endpoint attribute that represents the full endpoint for the graph.
# The class has three methods:
# create_graph: This method takes in parameters for the name, unit, type, and color of the graph and uses them to create the graph in the Pixela API. It sends a POST request to the graph_endpoint with the graph configuration as the request body.
# update_graph: This method takes in optional parameters for the name, unit, type, and color of the graph and updates the graph in the Pixela API with the provided values. It sends a PUT request to the graph_endpoint with the updated graph configuration as the request body.
# delete_graph: This method deletes the graph from the Pixela API by sending a DELETE request to the graph_endpoint.
class PixelaGraph(PixelaApi):
    def __init__(self, username, token, graph_id):
        super().__init__(username, token)
        self.graph_id = graph_id
        self.graph_endpoint = f"{self.base_endpoint}/{self.username}/graphs/{self.graph_id}"
    
    def create_graph(self, name, unit, graph_type, color):
        graph_config = {
            "id": self.graph_id,
            "name": name,
            "unit": unit,
            "type": graph_type,
            "color": color
        }

        response = self.post(endpoint=self.graph_endpoint, json=graph_config)
        print(response.text)

    def update_graph(self, name=None, unit=None, graph_type=None, color=None):
        graph_config = {}

        if name:
            graph_config["name"] = name
        if unit:
            graph_config["unit"] = unit
        if graph_type:
            graph_config["type"] = graph_type
        if color:
            graph_config["color"] = color

        response = self.put(endpoint=self.graph_endpoint, json=graph_config)
        print(response.text)

    def delete_graph(self):
        response = self.delete(endpoint=self.graph_endpoint)
        print(response.text)

# Next, we define a PixelaData class that also inherits from PixelaApi. This class represents a pixel in a graph and has methods to create, update, and delete a pixel:
class PixelaData(PixelaApi):
    def __init__(self, date, quantity):
        super().__init__()
        self.date = date
        self.quantity = quantity

    def create_pixel(self, graph_id):
        endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}"
        data = {
            "date": self.date,
            "quantity": self.quantity,
        }
        response = self.post(endpoint, json=data)
        response.raise_for_status()
        print(f"Pixel created: {response.text}")

    def update_pixel(self, graph_id):
        endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}/{self.date}"
        data = {
            "quantity": self.quantity,
        }
        response = self.put(endpoint, json=data)
        response.raise_for_status()
        print(f"Pixel updated: {response.text}")

    def delete_pixel(self, graph_id):
        endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}/{self.date}"
        response = self.delete(endpoint)
        response.raise_for_status()
        print(f"Pixel deleted: {response.text}")

# Finally, we can use these classes to create a habit tracker program. Here's an example of how we can use these classes to create a new graph and add pixels to the graph:
def main():
    # create a new graph
    graph = PixelaGraph("cycling", "Cycling Graph", "Km", "float", "ajisai")
    graph.create_graph()

    # add pixels to the graph
    today = datetime.now().strftime("%Y%m%d")
    pixel1 = PixelaData(today, "5.0")
    pixel1.create_pixel(graph.graph_id)

    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d")
    pixel2 = PixelaData(tomorrow, "8.0")
    pixel2.create_pixel(graph.graph_id)

    # update a pixel
    pixel1.quantity = "6.0"
    pixel1.update_pixel(graph.graph_id)

    # delete a pixel
    pixel2.delete_pixel(graph.graph_id)


if __name__ == "__main__":
    main()
   

