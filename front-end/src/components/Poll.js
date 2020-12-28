export const Poll = (props) => {
    return (
        <div className="poll" id={props.id}>
            <h2>Brazilian President</h2>
            <form id="poll-form">
                <div id="poll-options">
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
