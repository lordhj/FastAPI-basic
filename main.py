from enum import Enum
# from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from typing import List, Optional

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
# class Item(BaseModel):
#     name: str
#     description: Optional[str]=None
#     price: float
#     tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     fullname: str=None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The Id of item to get", ge=0, le=150),
#     q: str=None,
#     item: Item=None,
#     user: User,
#     importance: int = Body(...)
# ):
#     results={"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     if item:
#         results.update({"item:": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results



#---- Body - Fields ----
# class Item(BaseModel):
#     name: str
#     description: str =  Field(
#         None,
#         title="Description of item",
#         max_length=300
#     )
#     price: float = Field(..., gt=0)
#     tax: float = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item=Body(...)):
#     results = {"item_id": item_id, "iteml": item}
#     return results


#----------------------Body Nested Modelssd


# In-memory data store
items = []

# Pydantic model for data validation
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing_item in items:
        if existing_item["id"] == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item.dict())
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            items[index] = item.dict()
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")

