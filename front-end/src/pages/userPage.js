import '../styles/pages/userPage.css';
import {Link} from 'react-router-dom';

const Button = (props) => {
  return(
    <Link to={props.to}>
      <button type="button" id={props.id} className={props.className}>
        {props.children}
      </button>
    </Link>
  );
};

function UserPage() {
  return (
    <div id="user-page">
      <h1>Hi, Adriano!</h1>
      <div id="user-options">
        <Button className="option" to="/vote" id="voteLink">
          <p>Vote</p>
        </Button>
        <Button className="option" to="/myvotings" id="votingsLink">
          <p>My Votings</p>
        </Button>
        <Button className="option" to="/newvoting" id="newLink">
          <p>New Voting</p>
        </Button>
      </div>
    </div>
  );
};

export default UserPage;