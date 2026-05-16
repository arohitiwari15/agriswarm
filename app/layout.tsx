import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { SimulationProvider } from "@/components/SimulationProvider";
import { ThemeProvider } from "@/components/ThemeProvider";
import { ThemeToggle } from "@/components/ThemeToggle";

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
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem={false}
          disableTransitionOnChange
        >
          <SimulationProvider>
            <div className="flex flex-col min-h-screen bg-background text-foreground relative overflow-x-hidden">
              {/* Premium Background Blurs */}
              <div className="fixed top-0 left-[-10%] w-[40%] h-[400px] bg-accent-green/10 rounded-full blur-[120px] pointer-events-none z-0"></div>
              <div className="fixed bottom-[-10%] right-[-5%] w-[30%] h-[300px] bg-blue-500/10 rounded-full blur-[100px] pointer-events-none z-0"></div>

              <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md supports-[backdrop-filter]:bg-background/60">
                <div className="container flex h-16 items-center">
                  <div className="mr-8 flex items-center space-x-2">
                    <Link href="/" className="flex items-center space-x-2">
                      <span className="font-bold text-xl tracking-tight text-foreground">Agri-Swarm</span>
                      <Badge variant="outline" className="border-accent-green text-accent-green ml-2 hidden sm:inline-flex shadow-[0_0_10px_rgba(82,183,136,0.2)]">
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
                    <ThemeToggle />
                  </div>
                </div>
              </header>
              <main className="flex-1 relative z-10">{children}</main>
              <footer className="border-t border-border py-6 md:py-0 relative z-10 bg-background/50 backdrop-blur-sm">
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
        </ThemeProvider>
      </body>
    </html>
  );
}