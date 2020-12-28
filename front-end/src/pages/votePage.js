import { useState } from 'react';
import { Poll } from '../components/Poll';
import '../styles/pages/votePage.css';


function VotePage() {

  const [pollID, setPollID] = useState('');

  return (
    <div id="vote-page">
        <h1>Vote now!</h1>
        <div id="poll-search">
          <h2>Enter poll ID:</h2>
          <form id="poll-search-form">
            <input id="pollID" placeholder="ID" value={pollID} onChange={event => setPollID(event.target.value)}/>
            <button id="submit-button" type="submit">Search</button>
          </form>
        </div>
        <hr/>
        <Poll id="pollID"/>          
    </div>
  );
};

export default VotePage;