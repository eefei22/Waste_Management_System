# Waste Management System Prototype

A Flask-based prototype application designed to enhance waste management systems by integrating IoT and AI technologies. This solution addresses common issues such as incomplete garbage collection and inefficient resource management.

---

## Problem Statement

1. **Incomplete Garbage Collection**: Garbage collectors often fail to clear all trash thoroughly during collection rounds.
2. **Poor Technological Integration**: A lack of advanced technology in waste management systems results in inefficient operations and poor waste management outcomes.

---

## Description of the Solution

To tackle these challenges, this prototype integrates IoT technologies into the waste management system to optimize operations. Key components include:

1. **GPS Tracking**:
   - Tracks the real-time location of garbage trucks.
   - Ensures trucks follow the most efficient routes to collect all garbage.

2. **Garbage Level Sensors**:
   - Provides real-time data for algorithmic analysis.
   - Optimizes collection routes based on truck load capacity and route efficiency.

3. **CCTV Surveillance**:
   - Captures video input for AI image analysis.
   - Ensures all garbage in the environment is completely cleared.
  
 4. **Admin Dashboad**:
 - Admin can view and manage IoT devices and track the garbage truck.

These technologies provide a foundation for improved waste collection efficiency and better resource allocation.

---

## Technical Solutions

### 1. Flask Application
A web application designed for administrators to monitor IoT data inputs and manage the real-time garbage collection system.

#### Features:
1. **Efficient Route Calculation**:
   - Uses an optimization algorithm to determine the optimal route for garbage trucks.
   - Maximizes garbage collection before returning to the waste management center.
   
  ![Truck Map Optimizer and Log](https://github.com/user-attachments/assets/db8742ce-bcbd-4141-bc89-d7cd5b5b06a4)

2. **Real-Time Load Monitoring**:
   - Logs garbage truck activity using level sensors.
   - Updates the system with the current truck load (weight).

3. **CCTV Integration**:
   - Allows administrators to view live CCTV surveillance.
   - Ensures that the environment is free of uncollected garbage.
     
  ![1](https://github.com/user-attachments/assets/be1ea62b-e36c-4fa9-83fd-63ed5de0ec48)


---

## Project Structure
1. **Context Diagram**
   
   ![WhatsApp Image 2024-11-28 at 03 46 36_db8fd903](https://github.com/user-attachments/assets/325d8ad0-4f83-40f4-ad6f-0163ef1fbce5)
   
2. **ERD**
   
   ![WhatsApp Image 2024-11-28 at 17 47 45_5cc3430f](https://github.com/user-attachments/assets/a7f0d83b-c6dc-4a6e-8386-151827b3b22d)

3. **Directories**
   
   ![image](https://github.com/user-attachments/assets/5c328ca2-76ce-4787-86b6-81b67ddacb62)

- `GarbageTruck_Routing.py`: Contains route optimization algorithms.
- `app.py`: Main Flask application entry point.
- `myhackathon`: Contains HTML templates for the web interface.

---

## Getting Started

### Prerequisites

1. Python 3.x installed on your system.
2. MongoDB Atlas set up for database integration.
3. Flask and other required Python packages (see `requirements.txt`).

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/waste_management.git
   
2. Navigate to the project directory:
   ```bash
   cd waste_management
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://127.0.0.1:5000`.

