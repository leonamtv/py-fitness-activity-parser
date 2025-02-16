import json
import datetime

def __json_default(value):
    if isinstance(value, datetime.datetime):
        return dict(time=value.isoformat())
    else:
        return value.__dict__
    

def to_json(value):
    return json.dumps(value, default=__json_default)