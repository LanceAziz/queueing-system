"use client"
import Image from "next/image";
import logo from "../../../../public/Images/Logo.png"
import { useState, useEffect, useRef } from 'react'
import Print from "@/app/(components)/print/page";
import { useReactToPrint } from 'react-to-print';

export default function Services() {
    const services = [
        { "nameEN": "Cash", "nameAR": "خزنة" },
        { "nameEN": "Student Affair", "nameAR": "شئون طلبة" },
        { "nameEN": "leader", "nameAR": "ادارة" }
    ];

    const [clients, setClients] = useState([]);
    const [max, setMax] = useState(
        services.reduce((acc, service) => {
            acc[service.nameAR] = 0;
            return acc;
        }, {})
    );
    const [addedClient, setAddedClient] = useState({})
    const componentRef = useRef();
    const handlePrint = useReactToPrint({
        content: () => componentRef.current,
    });

    useEffect(() => {
        fetchClients();
    }, []);

    const fetchClients = async () => {
        const response = await fetch('http://127.0.0.1:8000/api/clients/')
        const data = await response.json();
        setClients(data);
        findMaxClients(data);
    };

    const findMaxClients = (clients) => {
        const maxValues = { ...max };

        clients.forEach(client => {
            if (maxValues.hasOwnProperty(client.client_type)) {
                maxValues[client.client_type] = Math.max(maxValues[client.client_type], client.client_num);
            }
        });
        setMax(maxValues);
    };

    const addClients = async (type) => {


        const now = new Date();
        const currentDate = now.toLocaleDateString();
        const currentTime = now.toLocaleTimeString();
        let newClientNum = ''
        if (type == 'شئون طلبة' && max[type] == 0) {
            newClientNum = max[type] + 500;
        } else {
            newClientNum = max[type] + 1;
        }

        const data = {
            "client_num": newClientNum,
            "client_type": type,
            "client_date": currentDate,
            "client_time": currentTime
        };
        console.log(data.client_date);
        console.log(data.client_time);
        // console.log(typeof(data.client_date));

        setAddedClient(data)

        const response = await fetch("http://127.0.0.1:8000/api/clients/create/", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            fetchClients();
        }
        handlePrint()
    };
    return (
        <main className="h-screen bg-light flex flex-col justify-center items-center text-dark">
            <div className="w-20">
                <Image src={logo} alt="المعهد العالي للدراسات" />
            </div>
            <h1 className="text-xl text-dark pb-4">المعهد العالي للدراسات المتطورة</h1>
            <div className="bg-semi-light text-dark rounded-3xl py-5 px-8 flex flex-col text-xl gap-3">
                {services.map(service => (
                    <button key={service.nameAR}
                        onClick={() => addClients(service.nameAR)}
                        className="bg-light hover:bg-primary hover:text-light transform duration-300 text-semi-dark px-6 py-3 rounded-full text-center">
                        عميل {service.nameAR}
                    </button>
                ))}
            </div>
            <div className="">
                <Print ref={componentRef} num={addedClient.client_num} type={addedClient.client_type} date={addedClient.client_date} time={addedClient.client_time} />
            </div>
            <table className="table-auto border-separate border-spacing-x-5 absolute top-0 left-0">
                <thead>
                    <tr>
                        <th>num</th>
                        <th>type</th>
                        <th>date</th>
                        <th>time</th>
                    </tr>
                </thead>
                <tbody>
                    {clients.map((client) => (
                        <tr key={client.client_time}>
                            <td className={max[client.client_type] === client.client_num ? 'text-red-600' : ''}>{client.client_num}</td>
                            <td>{client.client_type}</td>
                            <td>{client.client_date}</td>
                            <td>{client.client_time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </main>
    );
}
