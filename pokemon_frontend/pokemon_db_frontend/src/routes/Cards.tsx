import React, { useEffect, useState } from 'react'
import { useQuery } from 'react-query'
import axios from 'axios'
import CardDetails from './CardDetails'

type Card = {
    card_id: number
    card_name: string,
    hp: number,
    price: number,
    retreat_cost: number,
    stage: number
}

const Cards = () => {
    const [cards, setCards] = useState<Card[] | []>([])
    const [queryType, setQueryType] = useState("name")
    const [textQuery, setTextQuery] = useState("")
    const [minVal, setMinVal] = useState(0)
    const [maxVal, setMaxVal] = useState(0)

    useEffect(() => {
        axios.get("http://localhost:8080/cards").then(res => setCards(res.data))
    }, [])

    const handleQueryChange = (e: any) => {
        console.log("Here")
        setQueryType(e.target.value)
    }

    const handleSearch = (e: any) => {
        setTextQuery(e.target.value)

        if (e.target.value == "") {
            axios.get("http://localhost:8080/cards").then(res => setCards(res.data))
            return
        }

        if (queryType == "name") {
            axios.get(`http://localhost:8080/cards/search/${e.target.value}`)
            .then(res => setCards(res.data))
        } else if (queryType == 'type') {
            axios.get(`http://localhost:8080/cards/type/${e.target.value}`)
            .then( res => setCards(res.data))
        }
    }

    const handleNumericalSearch = (min: number, max: number) => {
        if (max < min) {
            max = min
            setMaxVal(max)
        }

        if (max == 0) {
            axios.get("http://localhost:8080/cards").then(res => setCards(res.data))
            return
        }

        if (queryType == 'hp') {
            axios.get(`http://localhost:8080/cards/hp/${min}-${max}`)
            .then( res => setCards(res.data))
        }
        else if (queryType == 'price') {
            axios.get(`http://localhost:8080/cards/price/${min}-${max}`)
            .then( res => setCards(res.data))
        }
        else if (queryType == 'retreat_cost') {
            axios.get(`http://localhost:8080/cards/retreat-cost/${min}-${max}`)
            .then( res => setCards(res.data))
        }
    }

    const handleMinChange = (e: any) => {
        setMinVal(e.target.value)
        handleNumericalSearch(e.target.value, maxVal)
    }

    const handleMaxChange = (e: any) => {
        setMaxVal(e.target.value)
        handleNumericalSearch(minVal, e.target.value)
    }

  return (
    <div className='flex flex-col items-center'>
        <h2>Querying localhost:8080/cards</h2>

        <form className='flex'
        onChange={handleQueryChange}>
            <label htmlFor="name">
                <div className='m-2 p-2 bg-white rounded-md text-black w-32 cursor-pointer'>
                    <input type="radio" id="name" value="name" name="query_type"/>
                    {" Name"}
                </div>
            </label>
            <label htmlFor="type">
                <div className='m-2 p-2 bg-white rounded-md text-black w-32 cursor-pointer'>
                    <input type="radio" id="type" value="type" name="query_type"/>
                    {" Type"}
                </div>
            </label>
            <label htmlFor="hp">
                <div className='m-2 p-2 bg-white rounded-md text-black w-32 cursor-pointer'>
                    <input type="radio" id="hp" value="hp" name="query_type"/>
                    {" HP"}
                </div>
            </label>
            <label htmlFor="price">
                <div className='m-2 p-2 bg-white rounded-md text-black w-32 cursor-pointer'>
                    <input type="radio" id="price" value="price" name="query_type"/>
                    {" Price"}
                </div>
            </label>
            <label htmlFor="retreat_cost">
                <div className='m-2 p-2 bg-white rounded-md text-black w-32 cursor-pointer'>
                    <input type="radio" id="retreat_cost" value="retreat_cost" name="query_type"/>
                    {" Retreat Cost"}
                </div>
            </label>
        </form>

        {queryType == 'name' || queryType == 'type' ? 
            <form className='m-2 p-2 bg-white'
            onChange={handleSearch}>
                <input type='text' className='p-2 w-full'
                value={textQuery}
                placeholder={`Search a ${queryType == "name" ? "Pokemon" : "Type"}`}/>
            </form>
            :
            <div className='m-2 p-2 bg-white'>
                <input className='m-2 p-2'
                onChange={handleMinChange} value={minVal}
                type="number" name="numerical" placeholder='Enter the min'/>
                <input className='m-2 p-2'
                onChange={handleMaxChange} value={maxVal}
                type="number" name="numerical" placeholder='Enter the max'/>
            </div>
        }

        <p>{minVal}</p>

        <div className='flex flex-wrap'>
            {cards && cards.map( card => (
                <div className='w-96' key={card.card_id}>
                    <CardDetails card={card} />
                </div>
            ))}
        </div>

    </div>
  )
}

export default Cards