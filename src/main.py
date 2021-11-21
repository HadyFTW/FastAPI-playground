from fastapi import FastAPI, Path, Query
from enum import Enum

app = FastAPI()

# [Limiting Allowed Values] list all the valid values for a specific kind of data - in our case: str.
class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


class UsersInfo(str, Enum):
    FULL_INFO = "full_info"
    LOW_INFO = "low_info"


class QueryType(int, Enum):
    PAGE_SIZE = 10


# we used ellipsis syntax here, to always required this path parameter[but, It doesn't matter, It will always be required as the docs said!]
@app.get("/users/{type}/{id}")
async def hello_world(type: UserType, id: int = Path(..., ge=1)):
    return {"type": type, "id": id}


# one solution is to define min and max length for the plate
# @app.get('/license-plates/{license}')
# async def get_license_platees(license: str = Path(..., min_length=9, max_length=9)):
#     return {"license": license}


# another one is to define a Regex pattern to validate the license plate number
@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$"), title="the license plate number"):
    return {"license": license, "info": title}


@app.get("/queries")
async def get_query_params(page: int = Query(..., gt=0,le=12), size: int = Query(10, gt=0, le=100)):
    return {"page": page, "size": size}




@app.get("/userss")
async def get_userss(format: UsersInfo = "low_info"):
    return {"format": format}