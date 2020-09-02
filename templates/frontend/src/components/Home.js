import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {

    return(
        <div> 
           
            <Link to="/signup">
                <button type="button" className="signup">
                 Sign Up
                </button>          
            </Link>
            
            <p className="or">or</p>
            
            <Link>
                <button type="button" className="login">
                 Login
                </button>
            </Link>
        
        </div>
    )
}

export default Home;