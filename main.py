from enum import Enum
from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/")
# async def post():
#     return {"message": "This is hello from post function"}



# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"id": item_id, "q": q}
#     return {"id": item_id}

# @app.get("/items/mycart")
# async def get_mycart():
#     return {"message": "This is my cart"}

# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"

# @app.get("/foods/{food}")
# async def get_food(food: FoodEnum):
#     if food==FoodEnum.vegetables:
#         return {"food": food, "message": "Healthy"}

#     if food.value == "fruits":
#         return {"food": food, "message": "Little Bit Healthy"}

#     return {"food": food, "message": "Ding Ding"}

# fake_db=[{"iname": "Foo"},
#          {"iname": "zoo"},
#          {"iname": "coo"},]

# @app.get("/name/{id}")
# async def list_names(id:int,skip: int=1, limit:int=10):
#     return {"dict": fake_db[skip: skip+limit], "msg":id}

# class Item(BaseModel):
#     name: str
#     description: Optional[str]=None
#     price: float
#     tax: Optional[float]=None

# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         pwt=item.price + item.tax
#         item_dict.update({'price_with_tax': pwt})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: Optional[str]=None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/items")
# async def read_items(q: Optional[str]=Query(None, max_length=6)):
#     results={'items': [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({'q': q})
#     return results

#--------body ---MULTIPLE PARAMETERS
class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    fullname: str=None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The Id of item to get", ge=0, le=150),
    q: str=None,
    item: Item=None,
    user: User,
    importance: int
):
    results={"item_id": item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item:": item})
    if user:
        results.update({"user": user})
    if importance:
        results.update({"importance": importance})
    return results