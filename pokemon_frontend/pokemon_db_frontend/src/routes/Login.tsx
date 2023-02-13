import axios from 'axios'
import React, { useState } from 'react'
import { useOutletContext } from 'react-router'

type Props = {
    email: string,
    password: string,
    userId: number | "None",
    setUserId: (x: number | "None") => void,
    setEmail: (x: any) => void,
    setPassword: (x: any) => void,
    loggedIn: boolean,
    setLoggedIn: (x: boolean) => void
}

const Login = () => {
    const {email, password, userId, setUserId, setEmail, setPassword, loggedIn, setLoggedIn}: Props = useOutletContext()
    const [statusCode, setStatusCode] = useState<number>()
    const handleSubmit = (e : any) => {
        e.preventDefault()

        axios.post("http://localhost:8080/login", {
            email: email,
            password: password
        })
        .then( res => {
            setStatusCode(res.status)
            if (res.status == 200) {
                setUserId(res.data.user_id)
                setLoggedIn(true)
            }
        })
    }

    const handleSignOut = (e: any) => {
        e.preventDefault()
        axios.post("http://localhost:8080/logout", {
            user_id: userId,
        })
        .then( res => {
            setStatusCode(res.status)
            if (res.status == 200) {
                setUserId("None")
                setLoggedIn(false)
            } else {
                console.log("Error signing out")
            }
        })
    }

  return (
    <div className='w-full'>
        {!loggedIn &&
        <form className='bg-white m-4 p-4 flex flex-col justify-center'
        onSubmit={handleSubmit}>
            <p className='text-black my-2'>Log in</p>
            <input type='text' placeholder='email' value={email}
            onChange={(e: any) => setEmail(e.target.value)}
            className='my-2 p-2'/>
            <input type='text' placeholder='password' value={password}
            onChange={(e: any) => setPassword(e.target.value)}
            className='my-2 p-2'/>

            <button type='submit' className='bg-slate-800 my-2'>Log in</button>
        </form>
        }

        {loggedIn && 
        <div>
            <form className='bg-white m-4 p-4 flex flex-col'
            onSubmit={handleSignOut}>
                <h1 className='text-black text-xl'>Successfully logged in</h1>
                <button type='submit' className='bg-slate-800 my-2'>Sign Out</button>
            </form>
        </div>
        }

        <pre>User ID: {userId}</pre>
        <pre>Status Code: {statusCode}</pre>
    </div>
  )
}

export default Login