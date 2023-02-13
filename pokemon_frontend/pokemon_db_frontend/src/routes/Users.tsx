import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

type User = {
    user_id: number,
    username: string,
    email: string,
    userpassword: string
}

const Users = () => {
    const [users, setUsers] = useState([])
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    useEffect(() => {
        axios.get("http://localhost:8080/users").then(res => setUsers(res.data))
    }, [])

    const handleSubmit = (e: any) => {
        e.preventDefault()

        axios.post("http://localhost:8080/users", {
            email: email,
            username: username,
            password: password
        })
        .then( res => console.log(res))

        setUsername("")
        setEmail("")
        setPassword("")

        axios.get("http://localhost:8080/users").then(res => setUsers(res.data))
    }
    
  return (
    <div className='w-full m-4'>
        <table className='w-full'>
            <thead>
                <tr className='w-full m-2 bg-white'>
                    <th className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>ID</th>
                    <th className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>Username</th>
                    <th className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>Email</th>
                    <th className='text-black px-2 border-b-4'>Password</th>

                </tr>
            </thead>
            <tbody>
            {users && users.map( (user: User) => (
                <tr key={`${user.username}-${user.user_id}`}
                className='w-full m-2 bg-white hover:bg-slate-200 cursor-pointer'>
                    <td className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>{user.user_id}</td>
                    <td className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>{user.username}</td>
                    <td className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>{user.email}</td>
                    <td className='text-black px-2 border-b-4'>{user.userpassword}</td>

                </tr>
            ))}
            </tbody>
        </table>
    
        <form className='bg-white m-4 p-4 flex flex-col'
        onSubmit={handleSubmit}>
            <p className='text-black my-2'>Add User</p>
            <input type='text' placeholder='username' value={username}
            onChange={(e: any) => setUsername(e.target.value)}
            className='my-2 p-2'/>
            <input type='text' placeholder='email' value={email}
            onChange={(e: any) => setEmail(e.target.value)}
            className='my-2 p-2'/>
            <input type='text' placeholder='password' value={password}
            onChange={(e: any) => setPassword(e.target.value)}
            className='my-2 p-2'/>

            <button type='submit' className='bg-slate-800 my-2'>Create</button>
        </form>
    </div>
  )
}

export default Users