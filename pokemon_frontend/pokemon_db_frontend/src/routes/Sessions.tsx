import axios from 'axios'
import React, { useEffect, useState } from 'react'

type Session = {
	session_id: number
	user_id: number
}

const Sessions = () => {
	const [sessions, setSessions] = useState([])
	useEffect(() => {
	  axios.get("http://localhost:8080/sessions").then(res => setSessions(res.data))
	}, [])

  return (
	<div className='w-full m-4'>
		{sessions &&
		<table className='w-full'>
			<thead>
				<tr className='w-full m-2 bg-white'>
					<th className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>Session ID</th>
					<th className='text-black px-2 border-b-4'>User ID</th>
				</tr>
			</thead>
			<tbody>
			{sessions.map( (session: Session) => (
				<tr key={`${session.session_id}-${session.user_id}`}
				className='w-full m-2 bg-white hover:bg-slate-200 cursor-pointer'>
					<td className='text-black px-2 border-r-4 border-b-4 border-r-red-100'>{session.session_id}</td>
					<td className='text-black px-2 border-b-4'>{session.user_id}</td>
				</tr>
			))}
			</tbody>
		</table>
		}
		{ !sessions &&
			<h1 className='text-3xl text-white'>No active sessions</h1>
		}
	</div>
  )
}

export default Sessions