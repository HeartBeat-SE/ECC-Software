# Emergency Signalling and ECC Functioning

This repository contains a simple Python program that simulates the functioning of the **Emergency Management System**.

Data about *First Responders* are stored in the following format:

```json
{
    "userId": "0001",
    "name": "Alessandro",
    "city": "Forlì",
    "coordinates": ["15", "70"]
}

```
Data about *available AEDs* are stored in the following format:

```json
{
    "aedId": "0001",
    "name": "Stazione",
    "coordinates": ["45", "80"]
}
```

Through coordinates, the system is able to locate both First Responders and AEDs, which are displayed on the map as follows:

![](plots.png)

## Emergency System Functioning
The program starts by collecting the coordinates about the emergency, manually inserted by the ECC operator, and then, it calculates the distance between the **emergency locations** and all the fist responders positioned in the same city.

At the same time, it identifies the closest AED to the emergency site and provides information about the closest responder and the closest defibrillator.

## Try the program

1. Clone the repository `git clone https://github.com/HeartBeat-SE/ECC-Software`
2. Execute the command `python emergency-system.py`
3. Follow the instruction on the terminal