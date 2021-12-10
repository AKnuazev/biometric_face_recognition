import logo from './logo.svg';
import './App.css';
import {useState} from "react";

function App() {
    const [recogResult, setRecogResult] = useState()
    const [chosenUserID, setChosenUserID]=useState("Пользователь не выбран")
    const [imageSource, setImageSource]=useState(logo)
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
    return (
        <div className="App">
            <header className="App-header">
                <div style={{flexDirection:'row'}}>
                    <img src={imageSource} className="App-logo" alt="logo"/>
                    <p>
                        Biometric Face Recognition
                    </p>
                    <button className="App-button" aria-pressed={true} onClick={()=>sendUserData({user_id: '1'})}>
                        1
                    </button>
                    <button className="App-button" onClick={()=>sendUserData({user_id: '2'})}>
                        2
                    </button>
                    <button className="App-button" onClick={()=>sendUserData({user_id: '3'})}>
                        3
                    </button>
                    <button className="App-button" onClick={()=>sendUserData({user_id: '4'})}>
                        4
                    </button>
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
            </header>
        </div>
    );
}

export default App;
