from fastapi import FastAPI, Header, Request
from .models import Timetable
from .firebase import get_user
from .database import (
    get_timetables,
    create_timetable,
    delete_timetable,
    update_timetable,
)
from .utils import get_token, gen_json_response

app = FastAPI()


@app.middleware("http")
async def authentication(request: Request, call_next):
    auth_header = request.headers.get("authorization", None)
    if not auth_header:
        return gen_json_response("Token is not provided.", 401)
    token = get_token(auth_header)
    if not token:
        return gen_json_response("Token is not provided.", 401)
    user = get_user(token)
    if not user:
        return gen_json_response("Token verification failed.", 401)
    request.state.uid = user
    response = await call_next(request)
    return response


@app.get("/api")
def index():
    return {"msg": "alive"}


@app.get("/api/{email}/{name}")
def get_timetable_api(request: Request, email: str, name: str) -> Timetable:
    user = request.state.uid
    if user != email:
        return gen_json_response("Permission denied.", 403)
    timetable = get_timetables(email=email, name=name)
    if timetable:
        timetable = timetable[0]
        return {"name": timetable["name"], "timetable": timetable["timetable"]}
    else:
        return gen_json_response("Not found.", 404)


@app.get("/api/{email}")
def get_timetable_by_user_api(request: Request, email: str) -> list[str]:
    user = request.state.uid
    if user != email:
        return gen_json_response("Permission denied.", 403)
    timetables = get_timetables(email=email)
    print(timetables)
    return [t["name"] for t in timetables]


@app.post("/api/create")
def create_timetable_api(request: Request, timetable: Timetable):
    timetable_json = timetable.dict()
    oid = create_timetable(
        request.state.uid, timetable_json["name"], timetable_json["timetable"]
    )
    if oid < 0:
        return gen_json_response("duplicate name", 400)
    else:
        return gen_json_response("success", 200)


@app.delete("/api/{email}/{name}")
def delete_timetable_api(request: Request, email: str, name: str):
    user = request.state.uid
    if user != email:
        return gen_json_response("Permission denied.", 403)
    d = delete_timetable(email=email, name=name)
    if d:
        return gen_json_response("success", 200)
    else:
        return gen_json_reposnse("failed", 404)


@app.put("/api/{email}/{name}")
def update_timetable_api(request: Request, email: str, name: str, update: dict):
    user = request.state.uid
    if user != email:
        return gen_json_response("Permission denied.", 403)
    res = update_timetable({"email": email, "name": name}, update)
    if res:
        return gen_json_response("success", 200)
    else:
        return gen_json_response("failed", 404)
