import { useState } from 'react';
import './index.css';

function App() {
  const [problem, setProblem] = useState('');
  const [answer, setAnswer] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSolve = async () => {
    if (!problem.trim()) {
      return;
    }

    setIsLoading(true);
    setError(null);
    setAnswer(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/solve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ problem: problem.trim() }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();
      setAnswer(data.answer || "I couldn't solve that problem.");
    } catch (err) {
      console.error('Error fetching solution:', err);
      setError('An error occurred while connecting to the server. Make sure the FastAPI backend is running on port 8000.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <div className="background-animation"></div>
      <div className="container">
        <header className="header">
          <h1>Mathiest</h1>
          <p>Your intelligent AI math companion</p>
        </header>

        <main className="glass-card">
          <div className="input-group">
            <textarea
              placeholder="Enter your math problem here... (e.g., Integrate x^2 from 0 to 5)"
              value={problem}
              onChange={(e) => setProblem(e.target.value)}
              className={error && !problem.trim() ? 'shake' : ''}
            ></textarea>
          </div>
          
          <button 
            onClick={handleSolve} 
            className="glow-btn"
            disabled={isLoading || !problem.trim()}
          >
            {isLoading ? (
              <div className="spinner"></div>
            ) : (
              <span>Solve</span>
            )}
          </button>

          {(answer || error) && (
            <div className="result-container">
              <h3>Solution</h3>
              <div className={`answer-content ${error ? 'error-text' : ''}`}>
                {error ? error : answer}
              </div>
            </div>
          )}
        </main>
      </div>
    </>
  );
}

export default App;
