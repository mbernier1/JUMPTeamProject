import { Link } from "react-router-dom";
import { Outlet } from "react-router-dom";

export default function Root() {
    return (
      <>
        <div className="mt-12">
          <h1 className="text-6xl font-bold underline m-4">Pokemon Cards Bootleg</h1>
          <div className="flex justify-end">
            <form id="search-form" role="search" 
            className="text-xl m-2 grow">
              <input
              className="w-full"
                id="text-search"
                aria-label="Search Cards"
                placeholder="Search Card"
                type="search"
                name="text-search"
              />
              <div
                id="search-spinner"
                aria-hidden
                hidden={true}
              />
              <div
                className="sr-only"
                aria-live="polite"
              ></div>
            </form>

            <div className="m-2 text-xl hover:underline ">
              <Link to={"cards"}>Cards</Link>
            </div>
            <div className="m-2 text-xl hover:underline ">
              <Link to={"users"}>Users</Link>
            </div>
            <div className="m-2 text-xl hover:underline ">
              <Link to={"reviews"}>Reviews</Link>
            </div>

          </div>

        </div>
        <div id="detail">
          <Outlet />
        </div>
      </>
    );
  }
  