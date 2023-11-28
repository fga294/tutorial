from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"List of the first {limit} published records"}
    else:
        return {"data": f"{limit} rows fetched"}


@app.get('/blog/{id}')
def show(id: int):
    return id


@app.get('/blog/{id}/comments')
def showcomments():
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {"data":  f'Blog with tilte: {blog.title}, has been created \
        successfully'}
