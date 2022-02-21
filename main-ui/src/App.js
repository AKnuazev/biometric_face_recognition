import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";
import {Lock} from "./Lock";


function App() {
    const [recogResult, setRecogResult] = useState()
    const [chosenUserID, setChosenUserID] = useState("Пользователь не выбран")
    const [image1Source, setImage1Source] = useState(logo)
    const [image2Source, setImage2Source] = useState(logo)
    const [gotLoginResult, setGotLoginResult] = useState(false)

    const [inAdmin, setInAdmin] = useState(false)

    const [name, setName] = useState('')
    const [username, setUsername] = useState('')
    const [ACL, setACL] = useState('')
    const [phone, setPhone] = useState('')
    const [email, setEmail] = useState('')

    const [loginUserID, setLoginUserID] = useState('')
    const [loginName, setLoginName] = useState('')
    const [loginUsername, setLoginUsername] = useState('')
    const [loginACL, setLoginACL] = useState('')
    const [loginPhone, setLoginPhone] = useState('')
    const [loginEmail, setLoginEmail] = useState('')

    const [responseText, setResponseText] = useState('')

    const [imageTaken, setImageTaken] = useState(false)
    const [firstRender, setFirstRender] = useState(true)
    const EXAMPLE_DOORS = [
        {
            'id': 1,
            'code': 12,
            "name": "Дверь 1",
            "users_indoor_list": [2]
        },
        {
            'id': 2,
            'code': 23,
            "name": "Дверь 2",
            "users_indoor_list": [2]
        },
        {
            'id': 3,
            'code': 34,
            "name": "Дверь 3",
            "users_indoor_list": [2]
        },
        {
            'id': 4,
            'code': 45,
            "name": "Дверь 4",
            "users_indoor_list": [2]
        },
    ]
    const [doors, setDoors] = useState(EXAMPLE_DOORS)
    useEffect(() => {
        console.log("[i] in effect", firstRender)
        if (firstRender) {
            const loadDoors = async () => {
                let response = await fetch('http://localhost:8000/api_v1/main/rooms', {
                    method: 'GET',
                    // headers: {
                    //     'Content-Type': 'application/json;charset=utf-8'
                    // },
                });
                let json = await response.json()
                return json
            }

            setFirstRender(false)
            loadDoors()
                .then(doors => setDoors(doors))
                .catch(e => {
                    console.warn(e)
                    setResponseText(JSON.stringify(e))
                })
            // .catch(e => alert(e))}
        }

    }, [])

    const sendUserData = async (userData) => {
        try {
            setChosenUserID(userData.user_id)
            let response = await fetch('http://localhost:8000/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(userData)
            });
            // let json = await response.json()
            let text = await response.text()
            setRecogResult(text)

        } catch (e) {
            console.log("[X]\t Error: userData loading failed:", e)
        }
    }
    const sendNewUserData = async () => {
        try {
            let userData = {
                name: name,
                username: username,
                ACL: ACL,
                email: email,
                phone: phone,
            }


            let response2 = await fetch('http://localhost:8000/api_v1/main/users', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(userData)
            });
            // let json = await response.json()
            // let text = await response.text()
            // setRecogResult(text)
        } catch (e) {
            console.log("[X]\t Error: userData loading failed:", e)
        }
    }
    const takePicture = async () => {
        try {
            let response1 = await fetch('http://localhost:8000/api_v1/main/users/take_photo/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
            });
            let json = await response1.json()
            if (json.success) {
                setImageTaken(true)
            }
        } catch (e) {
            console.log("[X]\t Error: take picture failed:", e)
        }
    }

    const login = async () => {
        try {
            setGotLoginResult(true)
            let response = await fetch('http://localhost:8000/api_v1/main/users/login/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                // body: JSON.stringify(userData)
            });
            let json = await response.json()
            console.log(json.success)
            if (json.success) {
                setRecogResult(json.success)
                if (json.data) {
                    console.log(json.data)
                    setResponseText(json.data)
                    // setImage1Source(json.data.photo_url)
                    // setImage2Source(json.data.photo_url)
                }
                // setLoginUserID(json.data.userId)
                // setLoginName(json.data.name)
                // setLoginUsername(json.data.username)
                // setLoginACL(json.data.acl)
                // setLoginPhone(json.data.phone)
                // setLoginEmail(json.data.email)
            } else {
                setResponseText('Not recognised')
            }
            // setChosenUserID(userData.user_id)
            // let text = await response.text()
        } catch (e) {
            console.log("[X]\t Error: login failed:", e)
        }
    }
    const goToAdmin = () => {
        setInAdmin(true)
    }
    return (
        <div className="App">
            <header className="App-header">
                {/*<div className="App-topbar">*/}
                {/*    <button className="App-topbar-btn" onClick={goToAdmin}>*/}
                {/*        Admin panel*/}
                {/*    </button>*/}
                {/*</div>*/}
                <div className="App-topbar">
                    <a className="App-topbar-btn" href="http://localhost:8000/admin">
                        Admin panel
                    </a>
                </div>
                <div style={{flexDirection: 'row'}}>
                    {!gotLoginResult && <img src={logo} className="App-logo" alt="logo"/>}
                    {gotLoginResult && <div style={{flexDirection: "row"}}>
                        <img src={image1Source} className="App-logo" alt="image1"/>
                        <img src={image2Source} className="App-logo" alt="image2"/>
                    </div>}
                    <p>
                        Biometric Face Recognition
                    </p>
                    <p style={{color: 'lightgray', fontSize: 25}}>
                        Press any lock to open
                    </p>
                    {/*<button className="Login-button" onClick={login}>*/}
                    {/*    Login*/}
                    {/*</button>*/}
                    {/*<button className="App-button" onClick={()=>sendUserData({user_id: '4'})}>*/}
                    {/*    4*/}
                    {/*</button>*/}
                </div>
                <div>
                    {
                        doors.map(door => <Lock door={door}/>)
                    }
                </div>
                <p className="App-result-area">
                    Response:<br/>
                    {responseText}
                    {/*userID: {userID}<br/>*/}
                    {/*Recognised: {recogResult}<br/>*/}
                    {/*Name: {loginName}<br/>*/}
                    {/*Username: {loginUsername}<br/>*/}
                    {/*ACL: {loginACL}<br/>*/}
                    {/*Phone: {loginPhone}<br/>*/}
                    {/*Email: {loginEmail}<br/>*/}
                </p>
                {/*<a*/}
                {/*  className="App-link"*/}
                {/*  href="https://reactjs.org"*/}
                {/*  target="_blank"*/}
                {/*  rel="noopener noreferrer"*/}
                {/*>*/}
                {/*  Learn React*/}
                {/*</a>*/}
                {/*{inAdmin &&*/}
                {/*<div>*/}
                {/*    <form onSubmit={sendNewUserData}>*/}
                {/*        <label>*/}
                {/*            Name:*/}
                {/*            <input type="text" value={name} onChange={setName}/>*/}
                {/*        </label>*/}
                {/*        <br/>*/}
                {/*        <br/>*/}
                {/*        <label>*/}
                {/*            Username:*/}
                {/*            <input type="text" value={username} onChange={setUsername}/>*/}
                {/*        </label>*/}
                {/*        <br/>*/}
                {/*        <br/>*/}
                {/*        <label>*/}
                {/*            Email:*/}
                {/*            <input type="text" value={email} onChange={setEmail}/>*/}
                {/*        </label>*/}
                {/*        <br/>*/}
                {/*        <br/>*/}
                {/*        <label>*/}
                {/*            Phone:*/}
                {/*            <input type="text" value={phone} onChange={setPhone}/>*/}
                {/*        </label>*/}
                {/*        <br/>*/}
                {/*        <br/>*/}
                {/*        <label>*/}
                {/*            ACL:*/}
                {/*            <input type="text" value={ACL} onChange={setACL}/>*/}
                {/*        </label>*/}
                {/*        <br/>*/}
                {/*        <br/>*/}
                {/*        {imageTaken && <input type="submit" value="Отправить"/>}*/}
                {/*        {!imageTaken && <input type="submit" value="Отправить" disabled/>}*/}
                {/*    </form>*/}

                {/*    <button onClick={takePicture}>*/}
                {/*        Take picture*/}
                {/*    </button>*/}

                {/*</div>*/}
                {/*}*/}
            </header>
        </div>
    );
}

export default App;
