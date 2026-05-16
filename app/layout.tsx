import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { SimulationProvider } from "@/components/SimulationProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Agri-Swarm | Precision Farming AI",
  description: "AI-powered precision farming platform using drone swarms and rover.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={inter.className}>
        <SimulationProvider>
          <div className="flex flex-col min-h-screen bg-background text-foreground">
            <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
              <div className="container flex h-16 items-center">
                <div className="mr-8 flex items-center space-x-2">
                  <Link href="/" className="flex items-center space-x-2">
                    <span className="font-bold text-xl tracking-tight text-white">Agri-Swarm</span>
                    <Badge variant="outline" className="border-accent-green text-accent-green ml-2 hidden sm:inline-flex">
                      <span className="h-1.5 w-1.5 rounded-full bg-accent-green mr-1.5 animate-pulse-dot"></span> System Active
                    </Badge>
                  </Link>
                </div>
                <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
                  <nav className="flex items-center space-x-6 text-sm font-medium text-text-secondary">
                    <Link href="/dashboard" className="transition-colors hover:text-foreground">Dashboard</Link>
                    <Link href="/detection" className="transition-colors hover:text-foreground">Detection</Link>
                    <Link href="/technology" className="transition-colors hover:text-foreground">Technology</Link>
                  </nav>
                </div>
              </div>
            </header>
            <main className="flex-1">{children}</main>
            <footer className="border-t border-border py-6 md:py-0">
              <div className="container flex flex-col items-center justify-between gap-4 md:h-24 md:flex-row text-text-muted">
                <p className="text-center text-sm leading-loose md:text-left">
                  ©️ 2025 Agri-Swarm. Indigenous R&D, India.
                </p>
                <div className="flex space-x-4 text-sm">
                  <Link href="/dashboard" className="hover:text-foreground">Dashboard</Link>
                  <Link href="/technology" className="hover:text-foreground">Technology</Link>
                </div>
              </div>
            </footer>
          </div>
        </SimulationProvider>
      </body>
    </html>
  );
}