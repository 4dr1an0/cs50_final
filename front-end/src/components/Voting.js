export const Voting = (props) => {
    return (
        <div className="voting" id={props.id}>
            <h2>Brazilian President</h2>
            <form id="voting-form">
                <div id="voting-options">
                    <div className="option">
                        <button type="button" >Bolsonaro 17</button>
                    </div>
                    <div className="option">
                        <button type="button" >Lula 13</button>
                    </div>
                </div>
                <button id="submit-button" type="submit"><strong>Vote</strong></button>
            </form> 
        </div>
    );
};
