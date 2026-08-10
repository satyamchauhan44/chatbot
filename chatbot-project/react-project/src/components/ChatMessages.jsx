import { useRef, useEffect } from 'react';
import { ChatMessage } from './ChatMessage';

function ChatMessages({ chatMessages, loading }) {
  const chatMessagesRef = useRef(null);

  useEffect(() => {
    const containerElem = chatMessagesRef.current;
    if (containerElem) {
      containerElem.scrollTop = containerElem.scrollHeight;
    }
  }, [chatMessages, loading]);

  return (
    <div className="chat-messages-container" ref={chatMessagesRef}>
      {chatMessages.map((msg) => (
        <ChatMessage
          key={msg.id}
          message={msg.message}
          sender={msg.sender}
        />
      ))}

      {loading && (
        <ChatMessage
          loading={true}
          sender="robot"
        />
      )}
    </div>
  );
}

export default ChatMessages;