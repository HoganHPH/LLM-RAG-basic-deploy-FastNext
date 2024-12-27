'use client';

import { useState, useEffect } from 'react';
import useSWR from 'swr';

import Spinner from '@/components/spinner';

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export default function HomePage() {
    const [msg, setMsg] = useState<string>("Loading...");
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState<string>("");
    const [loading, setLoading] = useState<boolean>(false);

    const { data, error, isLoading } = useSWR('http://localhost:8000', fetcher);

    useEffect(() => {
        if (isLoading) {
            setMsg("Loading...");
        } else if (error) {
            setMsg(`Error: ${error.message}`);
        } else if (data) {
            setMsg(data.message || "Ready for upload.");
        }
    }, [isLoading, error, data]);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            setFile(event.target.files[0]);
            setMessage(""); // Reset the message when a new file is selected
        }
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        setLoading(true); // Show spinner
        try {
            const response = await fetch("http://localhost:8000/api/indexing", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const responseData = await response.json();
                setMessage("Indexing successful!");
            } else {
                setMessage("Failed to upload file.");
            }
        } catch (error) {
            console.error("Upload error:", error);
            setMessage("An error occurred during upload.");
        } finally {
            setLoading(false); // Hide spinner
        }
    };

    return (
        <div className="mt-5 text-2xl text-yellow-400">
            <h1 className="text-center font-bold">Upload PDF</h1>
            <p className="text-center mt-2">{msg}</p>
            <div className="my-10 flex flex-col items-center justify-center gap-4 bg-gray-100 p-8 rounded-lg shadow-md max-w-lg mx-auto">
                <input
                    type="file"
                    accept="application/pdf"
                    onChange={handleFileChange}
                    className="block w-full text-sm text-gray-500 
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-lg file:border-0
                        file:text-sm file:font-semibold
                        file:bg-blue-50 file:text-blue-700
                        hover:file:bg-blue-100
                        focus:outline-none"
                />
                <button
                    onClick={handleUpload}
                    disabled={loading} // Disable button when loading
                    className={`bg-blue-600 text-white font-bold py-2 px-6 rounded-lg shadow transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 ${loading ? "opacity-50 cursor-not-allowed" : "hover:bg-blue-700"
                        }`}
                >
                    {loading ? "Uploading..." : "Indexing"}
                </button>
                {loading && <Spinner />} {/* Show spinner while loading */}
                {message && (
                    <p className="mt-4 text-center text-gray-600 font-medium">{message}</p>
                )}
            </div>
        </div>
    );
}
