from pydantic import BaseModel

class Machine(BaseModel):
    name: str
    os: str="Windows"
    cores: int=4
    ram: int=16
    ip_address: str
    disk_space: int=256


        