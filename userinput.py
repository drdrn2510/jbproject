from src.machine import Machine
import logging
from pydantic import ValidationError, field_validator
import subprocess



logging.basicConfig(
    level=logging.INFO,
    filename="./logs/machine.log",
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_machine():
    while True:
        try:
            vm_os = input("Enter OS for machine: ")
            vm_cores = input("Enter number of cores for machine: ")
            vm_ram = input("Enter RAM (in GB) for machine: ")
            vm_ip = input("Enter IP address for machine: ")
            vm_disk = input("Enter disk space (in GB) for machine: ")
            vm_name = input("Enter machine name: ")

            vm = Machine(
                name=vm_name,
                os=vm_os,
                cores=int(vm_cores),
                ram=int(vm_ram),
                ip_address=vm_ip,
                disk_space=int(vm_disk)
            )

            logging.info(f"Machine created successfully: {vm}")
            return vm  # exit the loop after successful creation

        except ValueError as ve:
            logging.error(f"Validation error: {ve}")
            print(f"Error: {ve}. Please try again.\n")
            # loop continues automatically to ask again

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"An unexpected error occurred: {e}. Please try again.\n")
            # loop continues automatically to ask again


def saveasjson(machine: Machine):
    try:
        instancesjson = "./config/instances.json"
        with open(instancesjson, 'a') as f:
            f.write(machine.model_dump_json() + "\n")   
        logging.info(f"Machine data saved to {instancesjson}")
    except Exception as e:
        logging.error(f"Error saving machine data to {instancesjson}: {e}")

def run_install_script():
    try:
        result = subprocess.run(['./scripts/install.sh'], check=True, capture_output=True, text=True)
        print(f"Installation script output: {result.stdout}")
        logging.info(f"Installation script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Installation script failed with error: {e.stderr}")
        logging.error(f"Installation script failed with error: {e.stderr}")
    except Exception as e:
        logging.error(f"Unexpected error running installation script: {e}")