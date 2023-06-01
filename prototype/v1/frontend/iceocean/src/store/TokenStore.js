export function setJWT(token, login, email){
    localStorage.setItem('jwt', token);
    localStorage.setItem('login', login);
    localStorage.setItem('email', email);
}


export function isAuthorized(){

    console.log(Object.keys)
    console.log(localStorage.getItem('jwt'))

    const jwt = localStorage.getItem('jwt')
    const login = localStorage.getItem('login')
    const email = localStorage.getItem('email')

    if (jwt != null && login != null && email != null){
        return true
    } else {
        return false
    }
}


export function isAuthorizedRouter(){

    const jwt = localStorage.getItem('jwt')
    const login = localStorage.getItem('login')
    const email = localStorage.getItem('email')
    
    if (jwt != null && login != null && email != null){
        return false
    } else {
        return true
    }
}


export function exitFromApp(){
    localStorage.clear()
}