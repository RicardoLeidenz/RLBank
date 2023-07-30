from account import Account
class Bank:
    def __init__(self, clients: list[Account] = []):
        self.clients = clients

    @property
    def clients(self):
        """ Getter for clients """
        return self._clients

    @clients.setter
    def clients(self, clients: list[Account]):
        """ Setter for clients """
        self._clients = clients
