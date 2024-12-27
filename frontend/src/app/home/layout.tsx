import type { Metadata } from "next";


export const metadata: Metadata = {
    title: "Basic RAG",
    description: "Basic RAG",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <>{children}</>
    );
}
