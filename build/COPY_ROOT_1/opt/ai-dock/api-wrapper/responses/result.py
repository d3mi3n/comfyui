from pydantic import BaseModel, Field
from typing import Dict

class Output(BaseModel):
    local_path: str = Field(default='')
    url: str = Field(default='')

class Result(BaseModel):
    id: str
    message: str = Field(default='Request accepted')
    status: str = Field(default='pending')
    comfyui_response: Dict = Field(default={})
    output: list[Output] = Field(default=[])
    timings: Dict = Field(default={})

