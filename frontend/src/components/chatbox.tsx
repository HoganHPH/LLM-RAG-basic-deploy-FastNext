import React, { useState, forwardRef, useImperativeHandle } from 'react';
import Spinner from '@/components/spinner';

interface ChatboxProps {
    chatMessages: { sender: string; text: string }[];
    onSendMessage: (message: string) => void;
    chatLoading: boolean;
}

const Chatbox = forwardRef((props: ChatboxProps, ref) => {
    const { chatMessages, onSendMessage, chatLoading } = props;
    const [inputText, setInputText] = useState<string>('');

    useImperativeHandle(ref, () => ({
        resetChatbox: () => {
            setInputText('');
        },
    }));

    const handleSend = () => {
        if (inputText.trim() === '') return;
        onSendMessage(inputText);
        setInputText('');
    };

    return (
        <div className="bg-white shadow-lg rounded-lg p-4 w-full sm:w-2/3 mx-auto text-sm">
            {/* Chat Messages */}
            <div className="h-64 overflow-y-auto border border-gray-300 rounded-lg p-3 bg-gray-50">
                {chatMessages.length === 0 ? (
                    <p className="text-gray-500 text-center">No messages yet...</p>
                ) : (
                    chatMessages.map((message, index) => (
                        <div
                            key={index}
                            className={`mb-2 ${message.sender === 'User' ? 'text-right' : 'text-left'}`}
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

            {/* Input and Button */}
            <div className="mt-4 flex">
                <input
                    type="text"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Type your message..."
                    className={`flex-1 border border-gray-300 rounded-l-lg p-2 focus:outline-none focus:ring focus:ring-blue-200 text-black ${chatLoading ? 'opacity-50 cursor-not-allowed' : ''
                        }`}
                    disabled={chatLoading} // Disable input when loading
                />
                <button
                    onClick={handleSend}
                    disabled={chatLoading} // Disable button when loading
                    className={`bg-blue-600 text-white font-bold px-4 py-2 rounded-r-lg transition ${chatLoading ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700'
                        }`}
                >
                    {chatLoading ? 'Waiting...' : 'Send'}
                </button>
            </div>

            {/* Spinner */}
            {chatLoading && <Spinner />} {/* Show spinner when chatLoading is true */}
        </div>
    );
});

export default Chatbox;
