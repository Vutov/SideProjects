import React, { Component } from 'react';
import { forIn } from 'lodash';
import Control from '../components/Control'
import { guessPassword } from '../models/user'
import { generatePasswords } from '../models/forcer'

export default class HomePage extends Component {
    constructor() {
        super();
        this.state = {
            passwords: [],
            data: {},
            intervals: {},
            startTime: new Date()
        }
    }

    componentDidMount() {
        let passwords = generatePasswords();
        this.setState({ passwords: passwords });
    }

    setInterval(userName, passwords) {
        let currentPasswordIndex = 0;
        let interval = setInterval(function () {
            let password = passwords[currentPasswordIndex++];
            if (!password){
                clearInterval(interval);
            }

            this.forcePassword(userName, password);
        }.bind(this), Math.random() * (160 - 150) + 150);

        let intervals = this.state.intervals;
        intervals[userName] = interval;
        this.setState({ intervals: intervals });
    }

    forcePassword(userName, password) {
        guessPassword({ username: userName, password: password },
            function (response) {
                let currentData = {
                    message: '',
                    status: '',
                    found: true,
                    password: password,
                    foundTime: new Date()
                }

                let data = this.state.data;
                data[userName] = currentData;
                this.setState({ data: data });

                let interval = this.state.intervals[userName];
                clearInterval(interval);
            }.bind(this),
            function (response) {
                let currentData = {
                    message: response.responseText,
                    status: response.statusText,
                    found: false,
                    password: password,
                    foundTime: this.state.startTime
                }

                if (!this.state.data[userName] || !this.state.data[userName].found) {
                    let data = this.state.data;
                    data[userName] = currentData;
                    this.setState({ data: data });
                }
            }.bind(this)
        );
    }

    onStart() {
        let startTime = new Date();
        this.setState({ startTime: startTime });

        this.setInterval('User1', this.state.passwords);
        this.setInterval('User2', this.state.passwords);
        this.setInterval('User3', this.state.passwords);
        this.setInterval('User4', this.state.passwords);
    }

    onStop() {
        forIn(this.state.intervals, function (interval) {
            clearInterval(interval);
        }, this);
    }

    render() {
        let Status = [];
        forIn(this.state.data, function (data, userName) {
            Status.push(
                <div key={userName} className='sameRow'>
                    <div>Username: {userName}</div>
                    <div>Found: {data.found.toString()}</div>
                    <div>Message: {data.message}</div>
                    <div>Status: {data.status}</div>
                    <div>Password: {data.password}</div>
                    <div>Found for seconds: {(data.foundTime - this.state.startTime) / 1000}</div>
                </div>);
        }.bind(this));

        return (
            <section>
                <h1>Brute Force</h1>
                <Control onStart={this.onStart.bind(this)} onStop={this.onStop.bind(this)} />
                <div>Started: {this.state.startTime.toLocaleString()}</div>
                {Status}
            </section>
        )
    }
}