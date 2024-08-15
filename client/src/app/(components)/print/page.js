import React, { forwardRef } from 'react';
import Image from "next/image";
import logo from "../../../../public/Images/Logo.png";

const PrintableComponent = forwardRef(({ num = 0, type = "---", date = "---", time = "---" }, ref) => {
    function reformatDate(dateString) {
        if (dateString === '---') {
            return '---';
        } else {
            const [month, day, year] = dateString.split("/");
            return `${day}/${month}/${year}`;
        }
    }

    return (
        <main ref={ref} className="flex flex-col items-start">
            <div className="px-16">
                <div className="w-40 my-5">
                    <Image src={logo} alt="المعهد العالي للدراسات" />
                </div>
                <div className="text-center">
                    <p className="text-4xl">{type}</p>
                    <p className="text-8xl">{num}</p>
                    <div dir="ltr" className="text-xl py-14">
                        <p>{reformatDate(date)}</p>
                        <p>{time}</p>
                    </div>
                </div>
            </div>
        </main>
    );
});

export default PrintableComponent;
