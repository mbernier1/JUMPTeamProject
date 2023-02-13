import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useOutletContext } from 'react-router'

type Props = {
  userId: number
}

type Review = {
  card_id: number,
  card_name: string,
  rating: number,
  review: string,
  username: string
}

const Reviews = () => {
  const [reviews, setReviews] = useState<Review[]>([])
  const {userId}: Props = useOutletContext()

  useEffect(() => {
    axios.get(`http://localhost:8080/user-reviews/${userId}`)
    .then(res => setReviews(res.data))
  }, [userId])
  

  return (
    <div className='w-full'>
      {reviews &&
      <div className='w-full'>
        {reviews.map( review => (
          <div key={`${review.card_id}-${review.username}`} className='w-full bg-white m-4 p-2 rounded-md'>
            <p className='text-black text-3xl'>{review.card_name}</p>
            <div className='flex'>
              <img src={`/pokemon_img/${review.card_name}-${review.card_id}.png`}
              className='m-2 w-32 h-32'></img>
              <div className='grow flex flex-col'>
                <p className='p-2 text-black'>{review.review}</p>
                <p className='text-black ml-auto mt-auto justify-self-end'>{review.username}</p>
              </div>
            </div>
          </div>
        ))}
      </div>}
    </div>
  )
}

export default Reviews