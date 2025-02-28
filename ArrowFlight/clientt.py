import pyarrow as pa
import pyarrow.flight as fl

class ArrowFlightClient:

    def __init__(self, location):
        self.location = location
        self.client = fl.connect(self.location)

    def fetch_data(self, ticket):
        # Use the ticket directly to fetch the data
        print(f"Requesting data for ticket: {ticket}")
        reader = self.client.do_get(ticket)

        # Read the data and print it
        for chunk in reader:
            # Each chunk contains a RecordBatch that can be converted to a pandas DataFrame
            print(f"Received chunk: {chunk}")
            batch = chunk.data
            df = batch.to_pandas()  # Convert the RecordBatch to a pandas DataFrame
            print(df)

    def close(self):
        self.client.close()


if __name__ == "__main__":
    location = "grpc://0.0.0.0:5005"  # Ensure this matches the server's location
    client = ArrowFlightClient(location)

    # Create a ticket (this can be any identifier for the request)
    ticket = fl.Ticket(b"example_ticket")  # Example ticket as bytes

    client.fetch_data(ticket)
    client.close()
