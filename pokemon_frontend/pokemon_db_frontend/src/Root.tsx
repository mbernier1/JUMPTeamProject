import React from 'react'
import { Link, Outlet } from 'react-router-dom'

const Root = () => {
  return (
    <div className='mt-6 flex flex-col items-center'>
        <h1 className='select-none'>Bootleg Pokémon Cards</h1>
        <div>
            <nav>
                <Link className='text-white text-2xl m-2 hover:underline' to={"/"}>Home</Link>
                <Link className='text-white text-2xl m-2 hover:underline' to={"cards"}>Cards</Link>
                <Link className='text-white text-2xl m-2 hover:underline' to={"users"}>Users</Link>
                <Link className='text-white text-2xl m-2 hover:underline' to={"reviews"}>Reviews</Link>
                <Link className='text-white text-2xl m-2 hover:underline' to={"sales"}>Sales</Link>
                <Link className='text-white text-2xl m-2 hover:underline' to={"sessions"}>Sessions</Link>
            </nav>
        </div>

        <main className='flex w-full'>
            <Outlet />
        </main>
    </div>
  )
}

export default Root