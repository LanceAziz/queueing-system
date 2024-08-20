"use client"
import Image from "next/image";
import { useState } from 'react';
import logo from "../../../../../public/Images/Logo.png"
import { useRouter } from 'next/navigation'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';

export default function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [visiblePass, setVisiblePass] = useState(false)
    const [valid, setValid] = useState(true)
    const router = useRouter();

    const handlePassVis = () =>{
        if (visiblePass){
            setVisiblePass(false)
        }else{
            setVisiblePass(true)
        }
    }

    const login = async (username, password) => {
        const userData = {
            "username": username,
            "password": password
        }

        const response = await fetch("http://127.0.0.1:8000/api/teller/login/", {
            method: "POST",
            body: JSON.stringify(userData),
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            setValid(false)
        } else {
            const { refresh, access } = await response.json();
            setValid(true)
            router.push('http://localhost:3000/tellers/dashboard');
            console.log("access token: " + access);
            console.log("refresh token: " + refresh);
            // console.log(teller.num);
            // console.log(teller.type);
            // console.log(response.json);
            
        }
    }

    return (
        <main className="h-screen bg-light flex flex-col justify-center items-center text-dark">
            <div className="w-20">
                <Image src={logo} alt="المعهد العالي للدراسات" />
            </div>
            <h1 className="text-xl text-dark pb-4">المعهد العالي للدراسات المتطورة</h1>
            <div className="bg-semi-light text-dark rounded-3xl py-5 px-8 flex flex-col text-lg">
                <input onChange={(e) => (setUsername(e.target.value))} className="rounded-full p-3 focus:outline-primary mb-2 transform duration-500 ps-10" placeholder="اسم المستخدم" />
                <div className="relative">
                    <input onChange={(e) => (setPassword(e.target.value))} className="rounded-full p-3 focus:outline-primary mb-2 transform duration-500 ps-10 relative" type={visiblePass?"text":"password"} placeholder="كلمة المرور" />
                    <FontAwesomeIcon onClick={handlePassVis} className="text-primary absolute left-2 top-2 bg-light rounded-full p-2" icon={visiblePass?faEyeSlash:faEye} />
                </div>
                {!valid && <div className="text-primary mb-2 text-center">محاولة غير صحيحة</div>}
                <button onClick={() => login(username, password)} className="bg-light hover:bg-primary hover:text-light transform duration-300 text-lg text-semi-dark px-6 py-3 rounded-full text-center">تسجيل دخول</button>
            </div>
        </main>
    )
}
