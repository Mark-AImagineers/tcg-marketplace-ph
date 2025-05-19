import { useState } from 'react';

export default function Login() {
    const [email, setEmail] = useState('');

    return(
        <div>
            <h1>Login</h1>
            <form>
                <label htmlFor="email">Email:</label><br />
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                /><br />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}