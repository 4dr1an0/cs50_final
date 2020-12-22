import { useState } from 'react';
import { Voting } from '../components/Voting';
import '../styles/pages/votePage.css';


function VotePage() {

  const [votingID, setVotingID] = useState('');

  return (
    <div id="vote-page">
        <h1>Vote now!</h1>
        <div id="voting-search">
          <h2>Enter voting ID:</h2>
          <form id="voting-search-form">
            <input id="votingID" placeholder="ID" value={votingID} onChange={event => setVotingID(event.target.value)}/>
            <button id="submit-button" type="submit">Search</button>
          </form>
        </div>
        <hr/>
        <Voting id="votingID"/>          
    </div>
  );
};

export default VotePage;