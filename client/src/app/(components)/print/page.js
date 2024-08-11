import logo from "../../../../public/Images/Logo.png"
import Image from "next/image";

export default function Print({ num = 0, type = "---", date = "---", time = "---" }) {
    function reformatDate(dateString) {
        if (dateString == '---') {
            return '---'
        } else {
            const [month, day, year] = dateString.split("/");
            return `${day}/${month}/${year}`;
        }

    }
    return (
        <main className="flex flex-col items-start bg-blue-400">
            <div className="bg-yellow-300 px-16">
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
}