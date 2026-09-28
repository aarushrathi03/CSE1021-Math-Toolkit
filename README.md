# CSE1021: Algorithmic Mathematical & Number Theory Toolkit (CLI) 

A modular, command-line Python application developed for **CSE1021: Introduction to Problem Solving and Programming** at **VIT Bhopal University**. 

## Project Overview 
This project provides a terminal-based computational suite covering core number theory algorithms, factoring techniques, array processing methods, and base conversions. It follows top-down algorithmic design principles and adheres to clean modular software architecture. 

## Project Structure 

'''CSE1021-Math-Toolkit
│ 
├── module                    # Package containing core logic modules 
│   ├── init.py               # Package marker 
│   ├── factoring_engine.py   # Euclidean GCD, Primes, Sieve, Square Root 
│   ├── sequence_analytics.py # Fibonacci, Modular Exponentiation, LCG Pseudo-Random 
│   ├── array_processor.py    # Array Reversal, Duplicate Removal, Partitioning 
│   ├── base_converter.py     # Base Conversions & ASCII Mappings 
│   ├── logger_service.py     # Activity Logging (NFR) 
│   └── validator_utils.py    # Input Validation & Error Handling (NFR) 
│ 
├── main.py                   # Main CLI Menu Driver 
├── statement.md              # Problem Statement & Scope Document 
├── execution.log             # Auto-generated execution log file 
└── README.md                 # Project Setup & User Guide
'''