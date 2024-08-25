# Tech Scam Analysis Tool

## Project Overview

This repository contains the code and resources developed as part of the King's Undergraduate Research Fellowship project titled **"Tech Scams: A One-to-One Analysis with Scammers"**. The project focuses on the development of a software tool that enables the analysis of tech support scams by simulating real-life scenarios where scammers take control of virtual machines.

### Objective

The primary goal of this project is to develop a tool that:
- Simulates a real-life environment where tech scammers can gain control over a user’s device.
- Monitors and records the actions taken by the scammers on the controlled device.
- Analyzes the changes made to the device's filesystem and network traffic during the scamming session.

### Methodology

- **Virtual Machines**: The tool uses Oracle VirtualBox to create virtual environments that simulate real user devices. This ensures that the analysis is conducted in a controlled and safe environment.
- **Python Scripts**: The project employs Python scripts to manage the virtual machines, capture screen recordings, monitor network traffic, and analyze filesystem changes.

## Installation

To get started with the Tech Scam Analysis Tool, follow the steps below:

### Prerequisites

- **Oracle VirtualBox**: Ensure that Oracle VirtualBox is installed on your machine. You can download it from [here](https://www.virtualbox.org/wiki/Downloads).
- **Python 3.x**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **VirtualBox Python Library (`pyvbox`)**: This library is required to interact with VirtualBox through Python. Install it using pip:
  ```bash pip install pyvbox ```
- **Other Dependencies**: Additional Python packages can be installed using:
```pip install -r requirements.txt```

### Cloning the Repository

Clone the repository to your local machine using:
```git clone https://github.com/riccardogugliermini/tech-scam-analysis.git \n cd tech-scam-analysis```

### Usage

The tool is divided into two main Python scripts:

1.	scam-analyzer.py: This script manages the virtual machine. It performs the following operations:
   - Starts up the virtual machine.
   - Recovers a snapshot of the machine.
   - Initiates screen recording and network traffic capture.
   - Waits for the scammer to take control of the machine.
   - Shuts down the machine and saves the final state.
2.	report.py: This script analyzes the virtual machine post-scam session. It compares the filesystem before and after the scammer’s activity and generates a report logging all created, edited, and deleted files.

### Running the Scripts

- To start the virtual machine and prepare for a scammer interaction, run:
```python scam-analyzer.py```
- 	After the scam session, analyze the changes by running:
```python report.py```

### Results

The analysis tool generates detailed reports on the modifications made by the scammer on the virtual machine, including:

- Files created
- Files edited
- Files deleted
- Network traffic details

These reports can be used to study the behavior of scammers and develop strategies to prevent future scams.

### Discussion

Tech support scams are increasingly becoming sophisticated and pose significant risks to users. This tool provides a safe and controlled environment to study such scams, helping researchers and cybersecurity professionals develop better detection and prevention methods.

### Conclusion

The Tech Scam Analysis Tool is a valuable resource for analyzing tech support scams in a controlled virtual environment. By simulating real-life scenarios, it offers insights into the methods used by scammers and helps in the development of more effective countermeasures.


