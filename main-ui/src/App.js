import logo from './logo.svg';
import './App.css';
import {useState} from "react";


function App() {
    const [recogResult, setRecogResult] = useState()
    const [chosenUserID, setChosenUserID] = useState("Пользователь не выбран")
    const [image1Source, setImage1Source] = useState(logo)
    const [image2Source, setImage2Source] = useState(logo)
    const [gotLoginResult, setGotLoginResult] = useState(false)

    const [inAdmin, setInAdmin] = useState(false)

    const [name, setName] = useState()
    const [username, setUsername] = useState()
    const [ACL, setACL] = useState()
    const [phone, setPhone] = useState()
    const [email, setEmail] = useState()

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
    const  sendNewUserData = async () => {
        try {
            let userData = {
                name:username
            }
            let response = await fetch('http://localhost:8000/users', {
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
    const login = async () => {
        try {
            setGotLoginResult(true)
            let response = await fetch('http://localhost:8000/login', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                // body: JSON.stringify(userData)
            });
            let json = await response.json()
            setImage1Source(json.data.photo_url)
            setImage2Source(json.data.photo_url)
            // setChosenUserID(userData.user_id)
            // let text = await response.text()
            setRecogResult(json.status)

        } catch (e) {
            console.log("[X]\t Error: login failed:", e)
        }
    }
    const goToAdmin = () => {

    }
    return (
        <div className="App">
            <header className="App-header">
                <div className="App-topbar">
                    <button className="App-topbar-btn" onClick={goToAdmin}>
                        Admin panel
                    </button>
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
                    <button className="Login-button" onClick={login}>
                        Login
                    </button>
                    {/*<button className="App-button" onClick={()=>sendUserData({user_id: '4'})}>*/}
                    {/*    4*/}
                    {/*</button>*/}
                </div>
                <p className="App-result-area">
                    userID: {chosenUserID}<br/>
                    {recogResult}
                </p>
                {/*<a*/}
                {/*  className="App-link"*/}
                {/*  href="https://reactjs.org"*/}
                {/*  target="_blank"*/}
                {/*  rel="noopener noreferrer"*/}
                {/*>*/}
                {/*  Learn React*/}
                {/*</a>*/}
                {inAdmin &&
                <form onSubmit={handleSubmit}>
                    <label>
                        Имя:
                        <input type="text" value={this.state.value} onChange={this.handleChange}/>
                    </label>
                    <input type="submit" value="Отправить"/>
                </form>
                }
            </header>
        </div>
    );
}

export default App;
