import pyarrow as pa
import pyarrow.flight as fl

class ArrowFlightServer(fl.FlightServerBase):

    def __init__(self, location):
        super().__init__(location)
        self.location = location  # Store the location as an attribute
        self.data = self.create_data()

    def create_data(self):
        # Sample data to be transferred
        data = {
            'id': [1, 2, 3],
            'value': [100, 200, 300]
        }
        table = pa.table(data)
        return table

    def do_get(self, context, ticket):
        # Handle the client request and send data
        print(f"Received request for ticket: {ticket}")
        return fl.RecordBatchStream(self.data)

    def start_server(self):
        # Start the Arrow Flight server
        print(f"Starting server at {self.location}")
        self.serve()  # Directly call the serve method to start the server

if __name__ == "__main__":
    location = "grpc://0.0.0.0:5005"
    server = ArrowFlightServer(location)
    server.start_server()
