from pydantic import BaseModel
from pydantic import AnyUrl


class Link(BaseModel):
    url: AnyUrl
    description: str
