import React from 'react';
import { Link } from 'react-router-dom';

const Signup = () => {

    return(
        <div>
             <h1 text="bold" className="sign">Sign Up</h1>
             <form>
                 <p className="name">Full Name</p>
                 <input className="input1"/>
                 <p className="email">Email</p>
                 <input className="input2"/>
                 <p className="password">Password</p>
                 <input className="input3"/>
                 <p className="confirm">Confirm Password</p>
                 <input className="input4"/>
             </form>
             <Link to="/address">
             <button className="account">Create Account</button>
             </Link>
        </div>
    )
}

export default Signup;