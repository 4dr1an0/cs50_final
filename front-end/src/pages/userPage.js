import '../styles/pages/userPage.css';
import {Link} from 'react-router-dom';

const Button = () => {};

function UserPage() {
  return (
    <div id="user-page">
      <h1>Hi, Adriano!</h1>
      <div id="user-options">
        <Button className="option">
            <Link to="/vote" id="voteLink">
                Create new user
            </Link>
        </Button>
        <Button className="option">
            <Link to="/myvotings" id="votingsLink">
                Create new user
            </Link>
        </Button>
        <Button className="option">
            <Link to="/newvoting" id="newLink">
                Create new user
            </Link>
        </Button>
      </div>
    </div>
  );
};

export default UserPage;