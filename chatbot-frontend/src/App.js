import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]); // Chat messages
  const [input, setInput] = useState(""); // User input

  // Send message to backend
  const sendMessage = async () => {
    if (input.trim() === "") return;

    // Append the user's message to the chat
    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput(""); // Clear input field

    try {
      // Send the user's message to the Flask backend
      const response = await axios.post(
        "https://0975-153-33-34-165.ngrok-free.app/webhook",
        {
          message: input,
        }
      );

      // Append the bot's response to the chat
      setMessages([
        ...newMessages,
        { sender: "bot", text: response.data.fulfillmentText || "No response" },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
      setMessages([
        ...newMessages,
        { sender: "bot", text: "Error: Unable to connect to the server." },
      ]);
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <div className="chat-box">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`chat-message ${
                msg.sender === "user" ? "user-message" : "bot-message"
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
