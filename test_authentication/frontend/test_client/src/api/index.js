import axios from "axios";


export function postNewRecord (record, jwt){
    return axios.post('http://127.0.0.1:5000/add_record', {
        record: record
    }, 
    {
        headers: {
            Authorization: `Bearer: ${jwt}`  
        }
    })

}


export function authenticate(login, password){
    return axios.post('http://127.0.0.1:5000/enter', {
        login: login,
        password: password
    })
}


export function register(email, login, password){
    return axios.post('http://127.0.0.1:5000/registration', {
        email: email,
        login: login,
        password: password
    })
}