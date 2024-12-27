import React, { useState } from 'react';

interface ChatboxProps {
    chatMessages: { sender: string; text: string }[];
    onSendMessage: (message: string) => void;
}

const Chatbox: React.FC<ChatboxProps> = ({ chatMessages, onSendMessage }) => {
    const [inputText, setInputText] = useState<string>('');

    const handleSend = () => {
        if (inputText.trim() === '') return;

        // Send the message to the parent via onSendMessage prop
        onSendMessage(inputText);

        // Clear the input field
        setInputText('');
    };

    return (
        <div className="bg-white shadow-lg rounded-lg p-4">
            <div className="h-64 overflow-y-auto border border-gray-300 rounded-lg p-3 bg-gray-50">
                {chatMessages.length === 0 ? (
                    <p className="text-gray-500 text-center">No messages yet...</p>
                ) : (
                    chatMessages.map((message, index) => (
                        <div
                            key={index}
                            className={`mb-2 ${message.sender === 'User' ? 'text-right' : 'text-left'
                                }`}
                        >
                            <p
                                className={`inline-block px-3 py-2 rounded-lg ${message.sender === 'User'
                                    ? 'bg-blue-500 text-white'
                                    : 'bg-gray-300 text-gray-800'
                                    }`}
                            >
                                <strong>{message.sender}: </strong> {message.text}
                            </p>
                        </div>
                    ))
                )}
            </div>
            <div className="mt-4 flex">
                <input
                    type="text"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Type your message..."
                    className="flex-1 border border-gray-300 rounded-l-lg p-2 focus:outline-none focus:ring focus:ring-blue-200"
                />
                <button
                    onClick={handleSend}
                    className="bg-blue-600 text-white font-bold px-4 py-2 rounded-r-lg hover:bg-blue-700 transition"
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default Chatbox;
