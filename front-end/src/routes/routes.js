import {BrowserRouter, Switch, Route} from 'react-router-dom';

import Login from '../pages/loginPage';
import CreateUser from '../pages/createUser';
import PrivateRoute from './privateRoute';
import UserPage from '../pages/userPage';
import MyPolls from '../pages/showMyPolls';
import NewPoll from '../pages/newPoll';
import VotePage from '../pages/votePage';

function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Login}/>
                <Route path="/newuser" component={CreateUser}/>
                {/* Authentication required */}
                <Route path="/id" component={UserPage}/>
                <Route path="/vote" component={VotePage}/>
                <Route path="/mypolls" component={MyPolls}/>
                <Route path="/newpoll" component={NewPoll}/>
            </Switch>
        </BrowserRouter>
    );
}

export default Routes;