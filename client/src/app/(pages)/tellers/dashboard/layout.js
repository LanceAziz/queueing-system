import ProtectedRoute from "@/app/(components)/protectedRoute/page";

export default function DashboardLayout({ children }) {
    return (
        <>
            <ProtectedRoute>
                {children}
            </ProtectedRoute>
        </>
    );
}
