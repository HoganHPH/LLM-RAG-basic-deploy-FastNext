import { Metadata } from "next";

import HomePage from "@/app/home/page";

export const metadata: Metadata = {
    title: "Basic RAG",
    description: 'This is a basic deployment of RAG!'
}

export default function Home() {
    return (
        <HomePage />
    );
}
