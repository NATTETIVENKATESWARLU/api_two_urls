import json

def valid_data(data):
    try:
        d=json.loads(data)
        valid=True
    except Exception:
        valid=False
    return valid