import { useState } from 'react';

export function ChatInput({ chatMessages, setChatMessages }) {
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);

  function saveInputText(event) {
    setInputText(event.target.value);
  }

  async function sendMessage() {
    if (!inputText.trim() || loading) return;

    const currentText = inputText;
    setInputText('');

    // 1. Add user message to UI immediately
    const newChatMessages = [
      ...chatMessages,
      {
        message: currentText,
        sender: 'user',
        id: crypto.randomUUID()
      }
    ];

    setChatMessages(newChatMessages);
    setLoading(true);

    try {
      // 2. Query your FastAPI backend on port 8000
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: currentText })
      });

      if (!response.ok) {
        throw new Error('Server connection error');
      }

      const data = await response.json();

      // 3. Add bot reply from database
      setChatMessages([
        ...newChatMessages,
        {
          message: data.reply,
          sender: 'robot',
          id: crypto.randomUUID()
        }
      ]);
    } catch (error) {
      // Fallback message if python server isn't running
      setChatMessages([
        ...newChatMessages,
        {
          message: 'Unable to connect to the backend server. Please make sure uvicorn is running on port 8000.',
          sender: 'robot',
          id: crypto.randomUUID()
        }
      ]);
    } finally {
      setLoading(false);
    }
  }

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      sendMessage();
    }
    if (event.key === 'Escape') {
      setInputText('');
    }
  };

  return (
    <div className="chat-input-component">
      <input
        placeholder="Ask about B.Tech, fees, eligibility, hostel..."
        size="30"
        value={inputText}
        onChange={saveInputText}
        onKeyDown={handleKeyDown}
        disabled={loading}
        className="chat-input"
      />
      <button
        onClick={sendMessage}
        disabled={loading}
        className="send-button"
      >
        {loading ? '...' : 'Send'}
      </button>
    </div>
  );
}