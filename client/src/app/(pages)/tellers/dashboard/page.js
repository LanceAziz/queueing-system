"use client"
import Image from "next/image";
import { useState } from 'react';
import logo from "../../../../../public/Images/Logo.png"
import { ACCESS_TOKEN } from "../../../constants";
import { useRouter } from 'next/navigation'

export default function Tellers() {

  const [noClients, setNoClients] = useState(false)
  const [currentClient, setCurrentClient] = useState(0);
  const [tellerNum, setTellerNum] = useState(null)
  const [tellerType, setTellerType] = useState(null)
  const router = useRouter()


  const next_client = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/clients/serve/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem(ACCESS_TOKEN)}`,
      },
    });
    if (response.ok) {
      const data = await response.json();
      console.log("success");
      console.log(data.current_client);
      setCurrentClient(data.current_client);
      setTellerNum(data.teller_num);
      setTellerType(data.teller_type);
      setNoClients(false)
    } else if (response.status === 404) {
      setNoClients(true)
    } else if (response.status === 401) {
      router.push('http://localhost:3000/tellers/login')
    }
  }

  return (
    <main className="h-screen bg-light flex flex-col justify-center items-center text-dark">
      <div className="w-20">
        <Image src={logo} alt="المعهد العالي للدراسات" />
      </div>
      <h1 className="text-xl text-dark">المعهد العالي للدراسات المتطورة</h1>
      <h2 className="pb-4 text-lg text-dark">اهلاً بك، مستخدم <span className="text-primary">({tellerType})</span> شباك رقم <span className="text-primary">({tellerNum})</span></h2>
      <div className="bg-semi-light text-dark rounded-3xl py-5 px-8 flex flex-col text-xl">
        <div className="pb-5 text-center">عميل رقم: <span>{currentClient}</span></div>
        {noClients && <div className="text-primary mb-2 text-center">لا يوجد عملاء</div>}
        <button onClick={next_client} className="bg-light hover:bg-primary hover:text-light transform duration-300 text-semi-dark px-6 py-3 rounded-full text-center">العميل التالي</button>
      </div>
    </main>
  );
}
