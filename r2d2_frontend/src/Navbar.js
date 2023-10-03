// src/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="/">R2D2</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <Link class="nav-link" to="/marketgpt">MarketGPT <span class="sr-only">(current)</span></Link>
                    </li>
                    <li class="nav-item active">
                        <Link class="nav-link" to="/email">Automate Email Send <span class="sr-only">(current)</span></Link>
                    </li>
                    <li class="nav-item active">
                        <Link class="nav-link" to="/socialmedia">Automate Social Media Post <span class="sr-only">(current)</span></Link>
                    </li>

                </ul>
                <form class="form-inline my-2 my-lg-0">
                </form>
            </div>
        </nav>
    );
}

export default Navbar;