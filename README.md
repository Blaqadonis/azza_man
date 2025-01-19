# **Azza Man** 
### **Your AI-powered personal Financial Assistant**
#### **Creator - [🅱🅻🅰🆀](https://www.linkedin.com/in/chinonsoodiaka/)**

![azaman7](https://github.com/user-attachments/assets/58e8ac70-2d16-4809-88a0-d44631e36964)

![Screen Recording - Jan 19, 2025-VEED](https://github.com/user-attachments/assets/0ee60f25-d1f7-4f2e-8029-b916a23dcdc7)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Node and Function Descriptions](#node-and-function-descriptions)
- [Contributing](#contributing)
- [License](#license)


## Project Overview
Azza Man is a dynamic AI-driven personal financial assistant designed to help users manage their finances effortlessly. With features like budgeting, expense tracking, and insightful financial analysis, Azza Man simplifies the financial journey for users, making it easier to stay on top of their financial health.

## Features
- **Effortless Budgeting**: Create and manage your monthly budget with ease.
- **Expense Tracking**: Seamlessly track your expenses and gain insights into your spending habits.
- **AI-Powered Insights**: Receive valuable insights powered by artificial intelligence to help you make informed financial decisions.
- **User-Friendly Interface**: A clean and intuitive interface that enhances user experience.
- **Real-Time Interaction**: Engage in real-time conversations with Azza Man to get instant assistance.

## Architecture
The architecture of Azza Man consists of several key components:
- **Frontend**: Built using Streamlit, providing an interactive user interface.
- **Backend**: Utilizes LangChain for processing user inputs and generating responses.
- **Graph Structure**: Implements a state graph to manage the flow of conversation and actions.

![azzaman_architecture](https://github.com/user-attachments/assets/2abd3d5b-57f5-4590-b746-d5b104eca89a)


## Installation
To set up Azza Man locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Blaqadonis/azza_man.git
   cd azza-man
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set up environment variables**: Create a .env file in the root directory and add your API keys:
   ```bash
   GROQ_API_KEY=your_api_key_here
   LANGCHAIN_API_KEY=your_api_key_here

## Usage
* To run the Azza Man application, execute the following command:
   ```bash
   streamlit run app.py
* Open your web browser and navigate to [local server](http://localhost:8501/) to interact with Azza Man.

## Nodes and Function Descriptions

**Overview of Nodes**
Azza Man's functionality is organized into various nodes, each responsible for specific tasks within the application. Below is a detailed description of each node and its purpose:

   * **Landing Page Node**:
   
   Displays the introduction to Azza Man, including the logo and key features.
   Provides a user-friendly entry point to the application.
   
   * **Chat Page Node**:
   
   Facilitates real-time interaction between the user and Azza Man.
   Handles user inputs and displays responses from the AI.
   
   * **Budget Registrar Node**:
   
   Manages the creation and updating of user budgets.
   Allows users to set financial goals and track their progress.
   
   * **Expense Registrar Node**:
   
   Handles the logging of user expenses.
   Provides insights into spending patterns and areas for improvement.
   
   * **Expert Registrar Node**:
   
   Connects users with financial advice and expert insights.
   Offers personalized recommendations based on user data.
   
   * **Summarize Conversation Node**:
   
   Compiles the conversation history and provides a summary to the user.
   Helps users reflect on their financial discussions with Azza Man.

## Node and Function Descriptions

   * **assistant(state: dict) -> str**

      Purpose: Routes the user query to the appropriate registrar or handles session control.
      Parameters:
      state: The application's current state, including messages and session information.
      Returns: The next node to route to or a session control indicator ('END').
     
  * **intro(state: State) -> State**
      
      Purpose: Introduces Azza Man to the user and identifies their needs.
      Parameters:
      state: The current state of the application.
      Returns: Updated state after the introduction.
    
 * **evaluator(state: dict) -> str**

      Purpose: Evaluates the user's response to the introduction.
      Parameters:
      state: The current application state, including messages and session information.
      Returns: The appropriate next node to route the user to or session control indicator ('END').
   
* **budget_registrar(state: Dict[str, Any]) -> Dict[str, Any]**

      Purpose: Handles the budget registry process, prompting the user for income, savings goal, and currency details.
      Parameters:
      state: The state containing conversation context and user data.
      Returns: Updated state with user's income and savings goal.
  
* **expense_registrar(state: State) -> State**

      Purpose: Handles the expense registry process, prompting the user for expense amounts and currency details.
      Parameters:
      state: The current state containing conversation context and user data.
      Returns: Updated state with the user's total expenses and currency.
  
* **expert_registrar(state: Dict[str, Any]) -> Dict[str, Any]**
      
      Purpose: Handles the financial expert registry process, prompting the user for income, expenses, savings goals, and currency. Updates the state accordingly.
      Parameters:
      state: The state containing conversation context and user data.
      Returns: Updated state with the user's financial details.
  
## Contributing
Contributions are welcome! 

## License
This project is licensed under the MIT License. See the LICENSE file for details.
