import { Button, App } from "antd"; // Added Divider
import { FcGoogle } from "react-icons/fc";
import React, {useContext} from 'react'; // Import React for FC
import { useTranslation } from "react-i18next";
import { host } from "../../../../api/aierhubFetch";
import { IUserContexts, UserContexts } from "../../../../contexts/user-contexts";


const GoogleLoginPage: React.FC = ({ 

}) => {
    const userContexts: IUserContexts = useContext<IUserContexts>(UserContexts);
    const { t } = useTranslation();

    const handleLogin = () => {
        userContexts.setIsShowLoginModal(false);
        userContexts.setIsShowLoginModelLoading(true);
        const currentPath = window.location.pathname;
        const redirectUri = encodeURIComponent(currentPath);
        window.location.href = `${host}/api/auth/google/login?redirect_uri=${redirectUri}`;
    };

    return (
        <Button
            onClick={handleLogin}
            className="flex items-center justify-center gap-3 border rounded-md px-4 py-2 shadow-sm transition h-10"
        >
            <FcGoogle size={20} />
            <span className="text-sm font-medium text-gray-700">{t("sign_in_with_Google")}</span>
        </Button>
    );
};

export default GoogleLoginPage;
