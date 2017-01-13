import React, { Component } from 'react';

export default class Control extends Component {
    render() {

        return (
            <div >
                <button onClick={this.props.onStart}>Start</button>
                <button onClick={this.props.onStop}>Stop</button>
            </div>
        )
    }
}