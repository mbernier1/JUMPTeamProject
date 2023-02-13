import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useOutletContext } from 'react-router-dom'
import CardDetails from './CardDetails'

type Card = {
    card_id: number
    card_name: string,
    hp: number,
    price: number,
    retreat_cost: number,
    stage: number
}

type Props = {
    userId: number
}

const Inventory = () => {
    const [cards, setCards] = useState<Card[]>([])
    const {userId}: Props = useOutletContext()

    useEffect(() => {
        axios.get(`http://localhost:8080/users/${userId}/cards`)
        .then(res => setCards(res.data))
    }, [userId])

  return (
    <div className='flex flex-wrap justify-center'>
        {cards && cards.map( card => (
            <div className='w-96' key={card.card_id}>
                <CardDetails card={card} />
            </div>
        ))}
    </div>
  )
}

export default Inventory