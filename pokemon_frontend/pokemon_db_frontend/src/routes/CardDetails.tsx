import React from 'react'

type Card = {
    card_id: number
    card_name: string,
    hp: number,
    price: number,
    retreat_cost: number,
    stage: number
}

interface props {
    card: Card
}

const CardDetails = ({card}: props) => {
    const mapStage = (stage: number) => {
        return stage == 0 ? "Basic Stage"
        : `Stage ${stage}`
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
                <p className='text-black text-xl'>{`$${card.price}`}</p>
            </div>
        </div>
  )
}

export default CardDetails