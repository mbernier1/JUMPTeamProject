import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"
import ErrorPage from './ErrorPage'
import './index.css'
import CardDetails from './routes/CardDetails'
import Root from './routes/root'
import Welcome from './routes/Welcome'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Welcome />
      },
      {
        path: "cards/:id",
        element: <CardDetails />
      }
    ]
  },
])

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
