# JBProject Infrastructure Simulator - Doron Hacham.

## Overview

JBProject is a Python-based infrastructure automation and simulation tool. It enables users to model, simulate, and automate IT infrastructure operations in a safe, testable environment. The project is designed for IT professionals, DevOps engineers, and developers who want to validate automation scripts, test infrastructure logic, or demonstrate workflows without impacting real systems.

## Features
- **Infrastructure Simulation:** Simulate machine and infrastructure operations using Python modules.
- **Configurable Instances:** Define and manage infrastructure setups via JSON configuration files.
- **User Input Handling:** Interactive user input for dynamic automation scenarios.
- **Logging:** Detailed logs for monitoring, debugging, and auditing automation runs.
- **Extensible Scripts:** Add or modify automation logic with custom scripts.

## Folder Structure
- `src/`: Core modules for machine and infrastructure simulation.
- `config/`: Configuration files (e.g., `instances.json`) for infrastructure definitions.
- `scripts/`: Utility scripts for setup and automation.
- `logs/`: Log files generated during simulation.

## Getting Started
1. Install dependencies from `requirements.txt`.
2. Configure infrastructure in `config/instances.json`.
3. Run the main simulator script (`infra_simulator.py`).

## Use Cases
- Test automation logic without affecting production systems.
- Demonstrate infrastructure workflows in a simulated environment.
- Develop and debug infrastructure scripts and configurations.

## Requirements
- Python 3.7 or higher
- See `requirements.txt` for dependencies

## License
This project is intended for internal use and demonstration purposes.
