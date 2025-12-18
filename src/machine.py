from pydantic import BaseModel ,ValidationError, field_validator
import logging
import ipaddress

logging.basicConfig(level=logging.INFO,filename="./logs/provisioning.log",
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Machine(BaseModel):
    name: str
    os: str="Windows"
    cores: int=4
    ram: int=16
    ip_address: str
    disk_space: int=256

    @field_validator('os')
    def validate_os(cls, v):
        allowed_os = ['Windows', 'Linux', 'macOS']
        if v not in allowed_os:
            raise ValueError(f"OS must be one of {allowed_os}")
        return v
    @field_validator('cores')
    def validate_cores(cls, v):
        if v <= 0 or v>64:
            raise ValueError("Cores must be a between 1 and 64")
        return v
    @field_validator('ram')
    def validate_ram(cls, v):
        if v < 4 or v>512:
            raise ValueError("RAM must be between 4 and 512 GB")
        return v    
    @field_validator('disk_space')
    def validate_disk_space(cls, v):
        if v < 128 or v>4096:
            raise ValueError("Disk space must be between 128 and 4096 GB")
        return v
    @field_validator('ip_address')
    def validate_ip_address(cls, v):
        try:
            ipaddress.ip_address(v)
        except ValueError:
            raise ValueError("Invalid IP address format")
        return v
    @field_validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0 or len(v)>20:
            raise ValueError("Name cannot be empty and must be at most 20 characters long")
        if set('\/:*?"<>|@~').intersection(v):
            raise ValueError("Name cannot contain special characters: \\/:*?\"<>|")
        return v.strip()
    
    def model_post_init(self, __context=None):
        logging.info(f"Machine created: {self.name}, OS: {self.os} , IP: {self.ip_address} , Cores: {self.cores} , RAM: {self.ram}GB , Disk Space: {self.disk_space}GB ")       
    