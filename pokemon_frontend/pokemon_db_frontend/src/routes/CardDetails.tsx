import axios from 'axios'
import React, { useState } from 'react'
import { useOutletContext } from 'react-router'

type Card = {
    card_id: number
    card_name: string,
    hp: number,
    price: number,
    retreat_cost: number,
    stage: number,
    quantity?: number
}

interface props {
    card: Card
}

const CardDetails = ({card}: props) => {
    const {userId}: any = useOutletContext()
    const [message, setMessage] = useState("")

    const mapStage = (stage: number) => {
        return stage == 0 ? "Basic Stage"
        : `Stage ${stage}`
    }

    const handlePurchase = (cardId: number) => {
        const waitMsg = (msg: string) => {
            setMessage(msg)
            setTimeout(() => setMessage(""), 3000)
        }

        if (userId == "None") {
            waitMsg("Please login")
            return
        }

        axios.post("http://localhost:8080/sales/handle-sale", {
            user_id: userId,
            items: [cardId],
        })
        .then(res => {
            if (res.status == 200) {
                waitMsg("Purchase successful")
            }
        })
    }

    return (
        <div className='flex flex-col items-center m-4 p-2 bg-white border-2 borde-red rounded-xl'>
            
            <div className='w-full flex py-2 border-y-2 border-red-400 justify-between items-center'>
                <p className='p-2 text-black bg-slate-300 rounded-md'>{mapStage(card.stage)}</p>
                <h2 className='text-xl text-black'>{card.card_name}</h2>
                <div className='flex flex-col justify-center items-center bg-red-700 w-12 h-12 rounded-full'>
                    <p className='text-white'>{card.hp}</p>
                    <p className='text-sm text-white'>hp</p>
                </div>
            </div>

            <div>
                <img className='w-48 h-48 text-black'
                src={`/pokemon_img/${card.card_name}-${card.card_id}.png`} alt={`${card.card_id}`}/>
            </div>

            <div>
                {!card.quantity && <p className='bg-green-200 p-2 text-black text-xl rounded-md cursor-pointer'
                onClick={(e: any) => {
                    e.preventDefault()
                    handlePurchase(card.card_id)
                }}
                >{`$${card.price}`}</p>}
                {card.quantity && <p className='flex justify-center bg-blue-200 p-2 w-12 text-black text-xl rounded-md'>{`${card.quantity}`}</p>}
                <pre className='text-black'>{message}</pre>
            </div>
        </div>
  )
}

export default CardDetails