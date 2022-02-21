// @flow
import * as React from 'react';
import {useState} from "react";


export function Lock({door}) {
    const [opened, setOpened] = useState(false)
    // const {door.door_id} = props
    const enterDoor = async () => {
        try {

            let response = await fetch('http://localhost:8000/api_v1/main/users/login?is_entrance=' + (opened ? '0' : '1') + '&door_id=' + door.code, {
                method: 'POST',
                // headers: {
                //     'Content-Type': 'application/json;charset=utf-8'
                // },
            });
            let json = await response.json()
            if (json.success) {
                setOpened(!opened)
            } else {
                alert(json.error)
            }
        } catch (e) {
            console.warn(e)
            setOpened(!opened)
        }
    }
    return (
        <span style={{padding: 20}}>
            <button onClick={enterDoor} style={{
                borderTopLeftRadius: 70,
                borderTopRightRadius: 70,
                padding: 15,
                backgroundColor: opened ? "#12D778" : "#FF5065",
                borderBottomLeftRadius: 20,
                borderBottomRightRadius: 20,
            }}>
                <div>
                    <div style={{
                        width: 100,
                        height: 70,
                        borderTopLeftRadius: 50,
                        borderTopRightRadius: 50,
                        backgroundColor: "#2e333b"
                    }}/>
                </div>
                <p  style={{fontFamily:'Segoe UI', fontSize:20, color:'white'}}>
                {door.name}
                </p>
                <text style={{fontFamily:'Segoe UI', fontSize:16, color: "#2e333b", fontWeight:'bold'}}>
                    {opened ? "Opened" : "Closed"}
                </text>
            </button>
        </span>
    );
}