from src.machine import Machine
from pydantic import ValidationError    
import logging
from userinput import create_machine,saveasjson,run_install_script




#create a new machine by user input
newvm =create_machine()
print(f"Created machine: {newvm.name}")

#save the new machine as json file
saveasjson(newvm)

#run install script on the new machine
run_install_script()




