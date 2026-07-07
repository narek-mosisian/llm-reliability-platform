// the casing around all sides

import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "LLM Reliability Platform",
  description:
    "Production-grade AI Reliability & Inference Platform for RAG-based LLM applications.",
};

// The layout is assigned fixed page content.
type RootLayoutProps = Readonly<{ // these props are not to be modified
  children: React.ReactNode;
}>;

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
