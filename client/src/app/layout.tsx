export const metadata = {
  title: 'Next.js',
  description: 'Generated by Next.js',
};
import SubmitProvider from './context/SubmitContext';
import './globals.css';
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <SubmitProvider>
        <body>{children}</body>
      </SubmitProvider>
    </html>
  );
}
