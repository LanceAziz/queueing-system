import "./globals.css";
import localFont from '@next/font/local'
import { config } from '@fortawesome/fontawesome-svg-core';
import '@fortawesome/fontawesome-svg-core/styles.css';
config.autoAddCss = false;

export const metadata = {
  title: "المعهد العالي للدراسات المتطورة",
  description: "المعهد العالي للدراسات المتطورة",
};

const FrutigerLT = localFont({
  src: [
    {
      path: '../../public/Fonts/FrutigerLTArabic-45Light.ttf',
      style: 'light'
    },
    {
      path: '../../public/Fonts/FrutigerLTArabic-55Roman.ttf',
      style: 'medium'
    },
    {
      path: '../../public/Fonts/FrutigerLTArabic-65Bold.ttf',
      style: 'bold'
    }
  ],
});

export default function RootLayout({ children }) {
  return (
    <html lang="ar" dir="rtl" className={FrutigerLT.className}>
      <body>{children}</body>
    </html>
  );
}
