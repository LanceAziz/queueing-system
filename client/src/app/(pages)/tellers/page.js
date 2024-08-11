"use client"
import Image from "next/image";
import { useEffect } from 'react';
import logo from "../../../../public/Images/Logo.png"

export default function Tellers() {
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
    <main className="h-screen bg-light flex flex-col justify-center items-center text-dark">
      <div className="w-20">
        <Image src={logo} alt="المعهد العالي للدراسات" />
      </div>
      <h1 className="text-xl text-dark">المعهد العالي للدراسات المتطورة</h1>
      <h2 className="pb-4 text-lg text-dark">اهلاً بك، مستخدم <span>1</span></h2>
      <div className="bg-semi-light text-dark rounded-3xl py-5 px-8 flex flex-col text-xl">
        <div className="pb-5 text-center">عميل رقم: <span>301</span></div>
        <button onClick={nextUser} className="bg-light hover:bg-primary hover:text-light transform duration-300 text-semi-dark px-6 py-3 rounded-full text-center">العميل التالي</button>
      </div>
    </main>
  );
}
