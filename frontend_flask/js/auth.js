// auth.js

function getToken() {
    return localStorage.getItem("token");
}

function getRoles() {
    try {
        return JSON.parse(localStorage.getItem("roles")) || [];
    } catch (e) {
        return [];
    }
}

function getUser() {
    try {
        return JSON.parse(localStorage.getItem("user")) || null;
    } catch (e) {
        return null;
    }
}

function clearAuth() {
    localStorage.removeItem("token");
    localStorage.removeItem("roles");
    localStorage.removeItem("user");
}

function protectPage(requiredRoles = []) {
    const token = getToken();

    if (!token) {
        window.location.href = "login.html";
        return;
    }

    const roles = getRoles();

    if (requiredRoles.length > 0) {
        const hasAccess = roles.some(role => requiredRoles.includes(role));

        if (!hasAccess) {
            window.location.href = "unauthorized.html";
            return;
        }
    }
}
