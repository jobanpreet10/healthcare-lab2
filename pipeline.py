"""pipeline.py -- Healthcare Claims Pipeline."""


def extract():
    """Return dummy raw claims."""
    return [
        {"id": 1, "patient": "Alice", "amount": 500, "status": "pending"},
        {"id": 2, "patient": "Bob", "amount": None, "status": "approved"},
        {"id": 3, "patient": "Carol", "amount": 200, "status": "rejected"},
    ]


def transform(claims):
    """Fill null amounts and remove rejected claims."""
    result = []
    for c in claims:
        if c["status"] == "rejected":
            continue
        c["amount"] = c["amount"] if c["amount"] is not None else 0
        result.append(c)
    return result


def load(claims):
    """Simulate load -- return final list."""
    return claims


def run():
    """Run full pipeline: extract -> transform -> load."""
    return load(transform(extract()))


if __name__ == "__main__":
    for claim in run():
        print(claim)
