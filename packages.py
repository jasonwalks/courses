class Package:
    def __init__(self, id, sender, recipient, weight):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.id}: {self.sender} to {self.recipient}, {self.weight} kg"
    
    def cal_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
# packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    packages = [
        Package(id=1, sender="Alice", recipient="Bob", weight=10),
        Package(id=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    for package in packages:
        print(f"{package} costs ${package.cal_cost(cost_per_kg=2)}")
    #    print(f"Package {package.id}: {package.sender} to {package.recipient}, {package.weight}")

    #for package in packages:
    #   print(package.id)

main()