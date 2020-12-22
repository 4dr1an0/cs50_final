import '../styles/pages/loginPage.css';
import {Link} from 'react-router-dom';
import {useState} from 'react';

function Login() {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <div id="login-page">
      <h1>Welcome to Voter!</h1>
      <h2>Sign in to vote...</h2>
      <div className="login-interface">
          <form className="login-form">
            <div className="input-block">
              <input id="email" value={email} onChange={event => setEmail(event.target.value)} placeholder="Email"></input>
            </div>
            <div className="input-block">
            <input id="password" value={password} onChange={event => setPassword(event.target.value)} placeholder="Password"></input>
            </div>
            <Link to="/newuser" id="newuser-link">
                Create new user
            </Link>
            <button type="submit" id="submit-button">
              <p>Sign in</p>
            </button>
          </form>
      </div>
    </div>
  );
};

export default Login;
