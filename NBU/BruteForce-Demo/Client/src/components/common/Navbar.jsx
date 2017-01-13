import React, {Component} from 'react';

export default class Navbar extends Component {
    render() {
        return (
            <header id="menu" className='header'>
                {this.props.children}
            </header>
        );
    }
}