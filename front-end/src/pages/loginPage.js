import '../styles/pages/loginPage.css';
import {Link} from 'react-router-dom';

function Login() {
  return (
    <div id="login-page">
      <h1>Welcome to Voter!</h1>
      <h2>Sign in to vote...</h2>
      <div className="login-interface">
          <Link to="/newuser">
              Create new user
          </Link>
      </div>
    </div>
  );
};

export default Login;
