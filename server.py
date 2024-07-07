import yaml
import os

class Server:
    def __init__(self,config_path=None) -> None:
        with open(config_path,'r') as file:
            self.reader=yaml.safe_load(file)
        
        self.serverIP = self.reader.get("serverIP",None)
        self.localIP = self.reader.get("localIP",None)
        self.clients = []
        self.is_running = False

    def start_server(self):
        self.is_running = True
        print(f"Server started with IP: {self.serverIP}")
        print(f"Local IP: {self.localIP}")

    def stop_server(self):
        self.is_running = False
        print("Server stopped")
    
    def add_client(self, client):
        self.clients.append(client)
        print(f"Client {client} connected")
    def remove_client(self,client):
        if client in self.clients:
            self.clients.remove(client)
            print(f"Client {client} removed")
        else:
            print(f"Client {client} already not connected")
    def get_clients(self):
        return self.clients

if __name__ == "__main__":
    config_name="config.yaml"
    parent_directory=os.getcwd()
    print(parent_directory)
    config_path=os.path.join(parent_directory,config_name)

    server = Server(config_path)
    server.start_server()
    server.add_client("Client A")
    server.add_client("Client B")
    print(f"Clients connected: {server.get_clients()}")
    server.remove_client("Client A")
    server.stop_server()

