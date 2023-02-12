import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider
} from 'react-router-dom'
import { QueryClient, QueryClientProvider } from 'react-query'
import './index.css'
import NotFound from './NotFound'
import Root from './Root'
import Cards from './routes/Cards'
import Reviews from './routes/Reviews'
import Sales from './routes/Sales'
import Sessions from './routes/Sessions'
import Users from './routes/Users'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <NotFound />,
    children: [
      {
        path: "cards",
        element: <Cards />
      },
      {
        path: "users",
        element: <Users />
      },
      {
        path: "reviews",
        element: <Reviews />
      },
      {
        path: "sales",
        element: <Sales />
      },
      {
        path: "sessions",
        element: <Sessions />
      }
    ]
  },
])

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>,
)
