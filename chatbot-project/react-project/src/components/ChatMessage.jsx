import RobotProfileImage from '../assets/robot-image.png';
import UserProfileImage from '../assets/user-image.png';
import loadingSpinner from '../assets/loading-spinner.gif';

export function ChatMessage({ message, sender, loading }) {
  return (
    <div className={sender === 'user' ? 'chat-message-user' : 'chat-message-robot'}>
      {sender === 'robot' && <img src={RobotProfileImage} width="50" alt="Robot" />}
      
      <div className="message-text">
        {loading ? (
          <img src={loadingSpinner} width="40" alt="Loading..." />
        ) : (
          message
        )}
      </div>

      {sender === 'user' && <img src={UserProfileImage} width="50" alt="User" />}
    </div>
  );
}