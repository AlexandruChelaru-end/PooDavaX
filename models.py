from pydantic import BaseModel, Field

class PowInput(BaseModel):
    base: int
    exponent: int = Field(ge=0)

class FibInput(BaseModel):
    n: int = Field(ge=0)

class FactInput(BaseModel):
    n: int = Field(ge=0)
