from typing import Optional
from fastapi import FastAPI, HTTPException, Query
from utilities import filter_doughnuts, get_healthcheck_response

app = FastAPI()

@app.get('/healthcheck')
def handle_healthcheck():
    return {"status": get_healthcheck_response()}

@app.get('/doughnuts/info')
def get_doughnuts_info(max_calories: Optional[int] = Query(None), nuts: Optional[bool] = Query(None)):
    results = filter_doughnuts(max_calories, nuts)
    if not results:
        raise HTTPException(status_code=404, detail="No doughnuts found matching the criteria!")
    return {"results": results}
