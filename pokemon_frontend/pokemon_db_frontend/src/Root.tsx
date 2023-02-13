import React, { useState } from 'react'
import { Link, Outlet } from 'react-router-dom'

const Root = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [userId, setUserId] = useState<number | "None">("None")
    const [loggedIn, setLoggedIn] = useState(false)

    return (
        <div className='mt-6 flex flex-col items-center'>
            <h1 className='select-none'>Bootleg Pokémon Cards</h1>
            <div>
                <nav>
                    <Link className='text-white text-2xl m-2 hover:underline' to={"/"}>Home</Link>
                    <Link className='text-white text-2xl m-2 hover:underline' to={"cards"}>Cards</Link>
                    <Link className='text-white text-2xl m-2 hover:underline' to={"users"}>Users</Link>
                    {loggedIn && <Link className='text-white text-2xl m-2 hover:underline' to={"reviews"}>Reviews</Link>}
                    {loggedIn && <Link className='text-white text-2xl m-2 hover:underline' to={"inventory"}>Inventory</Link>}
                    <Link className='text-white text-2xl m-2 hover:underline' to={"login"}>{loggedIn ? "Signout" : "Login"}</Link>
                    <Link className='text-white text-2xl m-2 hover:underline' to={"sessions"}>Sessions</Link>
                </nav>
            </div>

            <main className='flex w-full'>
                <Outlet context={{email, password, loggedIn, userId, setUserId, setEmail, setPassword, setLoggedIn}}/>
            </main>
        </div>
  )
}

export default Root