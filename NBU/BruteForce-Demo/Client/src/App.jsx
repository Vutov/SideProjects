import React, { Component } from 'react';
import Navbar from './components/common/Navbar';
import Footer from './components/common/Footer';
import { Link } from 'react-router';
import './App.css';

class App extends Component {

    render() {
        return (
            <div id="app" className='wrapper'>
                <Navbar>
                    <Link to="/">Home</Link>
                    <Link to="/pass">Passwords</Link>
                </Navbar>
                <main className='main'>
                    {this.props.children}
                </main>
                <Footer />
            </div>
        )
    }
}

export default App;
