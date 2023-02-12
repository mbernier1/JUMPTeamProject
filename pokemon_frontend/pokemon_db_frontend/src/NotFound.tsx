import React from 'react'
import { useRouteError } from 'react-router-dom'

const NotFound = () => {
    const error: any = useRouteError()
  return (
    <div>
        <h1>404 Lol</h1>
        <p>
            <i>{error.statusText || error.message}</i>
        </p>
    </div>
  )
}

export default NotFound