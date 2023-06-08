import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
"""from visu.package.executors.segmentation import Segmentation
from visu.sdk.base.request import Request"""
import uvicorn
from fastapi import FastAPI

import json
from capsules.capsule.src.executors.segmentation import  UnetInferrer
from capsules.capsule.src.executors.trainer import Train
from sdks.visu.src.base.service import Service
from sdks.visu.src.base.bootstrap import Bootstrap
from sdks.visu.src.base.model import Request
app = FastAPI()


executors ={"Segmentation":{'Segmentation': UnetInferrer,
            "train" : Train
            }}

btstrp = Bootstrap(executors)
bootstrap = btstrp.run()



@app.post('/api')
async def api(request: Request):
    request_json = json.loads(request.json())
    json_data = json.dumps(request_json)
    resp = Service(json_data, executors, bootstrap).run()
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
