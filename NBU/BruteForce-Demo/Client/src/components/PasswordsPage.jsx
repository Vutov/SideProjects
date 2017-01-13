import React, { Component } from 'react';
import { getPasswords } from '../models/user'

export default class PasswordsPage extends Component {
    constructor() {
        super();
        this.state = {
            passwords: []
        }
    }

    componentDidMount() {
        getPasswords(function (data) {
            this.setState({passwords: data});
        }.bind(this));
    }

    render() {

        return (
            <section>
                <h1>Api Passwords</h1>
                {
                    this.state.passwords.map(function(password, i){
                        return <div key={i}>{password}</div>
                    })
                }
            </section>
        )
    }
}