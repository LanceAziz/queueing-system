"use client"
import Image from "next/image";
import { useEffect } from 'react';
import logo from "../../public/Images/Logo.png"
import Link from "next/link";

export default function Home() {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Enter') {
        nextUser();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);
  const nextUser = () => {
    console.log('nest user is on his way to your');
  }
  return (
    <div className="flex justify-center gap-5">
      <Link href={'/tellers/login'}>tellers</Link>
      <Link href={'/services'}>services</Link>
    </div>
  );
}
