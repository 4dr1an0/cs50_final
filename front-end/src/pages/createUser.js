import '../styles/pages/createUser.css';
import {useState} from 'react';

function CreateUser() {
  
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordCheck, setPasswordCheck] = useState('');

  return (
    <div id="newuser-page">
      <h1>Welcome to Voter!</h1>
      <h2>Create your account</h2>
      <div className="new-account">
          <form className="create-user-form">
            <div className="input-block">
              <input id="name" value={name} onChange={event => setName(event.target.value)} placeholder="Name"></input>
            </div>
            <div className="input-block">
              <input id="email" value={email} onChange={event => setEmail(event.target.value)} placeholder="Email"></input>
            </div>
            <div className="input-block">
            <input id="password" value={password} onChange={event => setPassword(event.target.value)} placeholder="Password"></input>
            </div>
            <div className="input-block">
            <input id="confirm-password" value={passwordCheck} onChange={event => setPasswordCheck(event.target.value)} placeholder="Confirm Password"></input>
            </div>
            <button type="submit" id="submit-button">
              <p>Create</p>
            </button>
          </form>          
      </div>
    </div>
  );
}

export default CreateUser;
