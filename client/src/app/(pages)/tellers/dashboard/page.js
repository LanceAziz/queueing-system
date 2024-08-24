"use client"
import Image from "next/image";
import { useState, useEffect, useRef } from 'react';
import logo from "../../../../../public/Images/Logo.png"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../../constants";
import { useRouter } from 'next/navigation'

export default function Tellers() {

  const [noClients, setNoClients] = useState(false)
  const [currentClient, setCurrentClient] = useState(0);
  const [tellerNum, setTellerNum] = useState(null)
  const [tellerType, setTellerType] = useState(null)
  const [audioUrl, setAudioUrl] = useState(null)
  const router = useRouter()
  const audioRef = useRef(null);

  useEffect(() => {
    get_teller_info();
  }, []);

  const get_teller_info = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/teller/info', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem(ACCESS_TOKEN)}`,
        },
      });

      if (!res.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await res.json();
      setTellerNum(data.teller_num)
      setTellerType(data.teller_type)
      console.log(data);
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  const play_audio = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/clients/audio/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem(ACCESS_TOKEN)}`,
      },
      body: JSON.stringify({})  // No additional text is needed here
    });

    if (response.ok) {
      const audioBlob = await response.blob(); // Get the audio blob from the response
      const audioUrl = URL.createObjectURL(audioBlob); // Create a URL for the blob
      const audio = new Audio(audioUrl);
      audio.play(); // Play the audio
    } else {
      console.error('Failed to fetch audio file');
    }
  }


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
      console.log();

    } else if (response.status === 404) {
      setNoClients(true)
    } else if (response.status === 401) {
      router.push('http://localhost:3000/tellers/login')
    }
    play_audio()
  }

  const logout = () => {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
    router.push('http://localhost:3000/tellers/login')
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
        <button onClick={logout} className="bg-light hover:bg-semi-dark hover:text-light transform duration-300 text-semi-dark px-6 py-3 rounded-full text-center mt-2">تسجيل خروج</button>
      </div >
      <audio className="hidden" ref={audioRef} src={audioUrl} />
    </main>
  );
}
