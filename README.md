# Mathiest

Mathiest is an intelligent AI math companion. It consists of a React/Vite frontend and a Python FastAPI backend powered by Langchain.

## Project Structure

- `frontend/`: Contains the React application built with Vite.
- `backend/`: Contains the FastAPI application and Langchain AI agents.

---

## Setup Instructions

Follow these steps to configure and run the project locally on your system.

### 1. Backend Setup

You need Python installed on your system. It is recommended to use a virtual environment.

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the `backend` folder and add any necessary API keys for Langchain/LLM models (e.g., `OPENAI_API_KEY`).

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

### 2. Frontend Setup

You need Node.js and npm installed on your system.

1. Open a new terminal window/tab and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm run dev
   ```

4. Open the link provided in the terminal (usually `http://localhost:5173`) in your web browser.

---

## Usage
1. Make sure both backend and frontend servers are running simultaneously.
2. Open the web interface in your browser.
3. Type in any mathematical problem in the input area and hit **Solve**!
