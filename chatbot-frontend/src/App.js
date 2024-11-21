import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]); // Chat messages
  const [input, setInput] = useState(""); // User input

  // Send message to backend
  const sendMessage = async () => {
    if (input.trim() === "") return;

    // Append user message to the chat
    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput(""); // Clear input field

    try {
      const response = await axios.post("http://127.0.0.1:5001/webhook", {
        message: input,
      });

      // Append bot's response to the chat
      setMessages([
        ...newMessages,
        { sender: "bot", text: response.data.fulfillmentText || "No response" },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
      setMessages([
        ...newMessages,
        { sender: "bot", text: "Error: Unable to reach the server." },
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
