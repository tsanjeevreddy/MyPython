class CompanyInfo:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def __repr__(self):
        return (
            f"CompanyDetails("
            f"symbol={self.symbol}, "
            f"name={self.name}, "
        )

    def to_dict(self):
        """Convert the model to a dictionary."""
        return {
            "symbol": self.symbol,
            "name": self.name,
        }
