from src.machine import Machine
from pydantic import ValidationError    
import logging
from userinput import create_machine,saveasjson,run_install_script





newvm =create_machine()
print(f"Created machine: {newvm.name}")

saveasjson(newvm)
run_install_script()



