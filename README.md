# FirstWeb3-DApp

**FirstWeb3-DApp** is my first decentralized application (DApp) built using Web3 technologies. The goal of this project is to help solve the problem of food scarcity during Christmas in Nigeria by enabling transparent and efficient donations using Ethereum smart contracts. The application is developed using **Solidity** for the smart contract, **Truffle** as the framework for smart contract management, **Flask** as the backend framework, and **Ganache** for the local Ethereum blockchain.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Smart Contract Creation](#smart-contract-creation)
5. [Truffle Configuration](#truffle-configuration)
6. [Deploying the Smart Contract](#deploying-the-smart-contract)
7. [Flask Backend Development](#flask-backend-development)
8. [Building the Frontend](#building-the-frontend)
9. [Running the Application](#running-the-application)
10. [What I Learned](#what-i-learned)
11. [How to Implement It](#how-to-implement-it)
12. [Contributing](#contributing)

## Project Overview
**FirstWeb3-DApp** enables users to donate Ethereum to help the poor during the Christmas season. The donations are managed through a smart contract on the Ethereum blockchain, ensuring transparency and security. This DApp provides a platform for people to contribute to a noble cause by interacting with the blockchain using an easy-to-use interface.

## Technologies Used
- **Solidity**: The language used to write the Ethereum smart contract.
- **Truffle**: A development framework for Ethereum smart contracts.
- **Flask**: A lightweight Python framework to create the backend API.
- **Web3.py**: A Python library for interacting with the Ethereum blockchain.
- **Ganache**: A personal Ethereum blockchain for testing.
- **HTML/CSS**: Frontend to create the user interface for donations.

## Setting Up the Development Environment
To set up this project on your local machine, follow these steps:

1. **Install Required Tools**:
   - Install **Node.js** (for Truffle and Ganache) from [Node.js](https://nodejs.org/).
   - Install **Python** (preferably version 3.10 or later) from [Python.org](https://www.python.org/downloads/).
   - Install **Truffle** globally:  
     ```bash
     npm install -g truffle
     ```
   - Install **Ganache** from the official website: [Ganache](https://trufflesuite.com/ganache/).
   - Install **Flask** and **Web3.py**:  
     ```bash
     pip install flask flask-cors web3
     ```

2. **Clone this repository**:
   ```bash
   git clone https://github.com/Bax-dev/Web3-DApp.git
   cd Web3-DApp

3. **Install dependencies for Truffle and Flask**:
   ```bash 
   npm install 

4. **Smart Contract Creation**:
   ```bash 

    In the contracts/ folder, I created a Solidity smart contract called ChristmasAid.sol which contains functions to:

    Accept donations (donate function).
    Allow the contract owner to distribute funds to the recipients (distributeFunds function).


## What I Learned
- **Web3 Development**: I learned how to interact with the Ethereum blockchain using Web3.js and Web3.py.
- **Smart Contracts**: I learned how to write, deploy, and interact with smart contracts using Solidity and Truffle.
- **Backend Development**: I used Flask to build a backend that communicates with the blockchain and serves the frontend.
- **Frontend Development**: I built a simple and user-friendly HTML interface for interacting with the smart contract.

## How to Implement It
**To implement this project**:
 ```bash 
   Follow the setup instructions in the Setting Up the Development Environment section.
   Write the smart contract using Solidity, deploy it with Truffle, and interact with it using Web3.py in Flask.
   Create a user-friendly HTML interface that allows users to interact with the smart contract and donate funds.